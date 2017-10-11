from .models import CATEGORIES,ICON
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpRequest 
from datetime import datetime, date

#START INDEX VIEW
#	MAIN PAGE VIEW 
#	SHOW LAST ICONS ADDED TO DATABASE
class IndexView(generic.ListView):
    template_name= 'web/index.html'
    model= ICON
    context_object_name= 'viewIcons' #chizi ke dar template fara mikhanim
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        current_month = datetime.now().month
        context['allIcons'] = ICON.objects.all()
        context['mustView'] = ICON.objects.filter(published_date__month=current_month).order_by('-views')[:3]
        return context

    def get_queryset(self):
        return ICON.objects.all().order_by('-published_date')
#
#END INDEX VIEW

#START INDEX VIEW
#   MAIN PAGE VIEW 
#   SHOW LAST ICONS ADDED TO DATABASE
class bests(generic.ListView):
    template_name= 'web/bests.html'
    model= ICON
    context_object_name= 'viewIcons' #chizi ke dar template fara mikhanim
    paginate_by = 9

    def get_queryset(self):
        return ICON.objects.all().order_by('-views')
#
#END INDEX VIEW


#START ICONS SINGLE VIEW
#
#	SHOW SPECIEFIED ICONS
def singlepage(request, thisicon_id):
    icon = get_object_or_404(ICON, id=thisicon_id)
    t = ICON.objects.get(id=thisicon_id)
    t.views = t.views + 1
    t.save()

    
    relatedIcon = ICON.objects.filter(name__contains=icon.name).exclude(id = thisicon_id)
    #contains= Case-sensitive containment test.
    relatedIconnotFound = ICON.objects.all().order_by('?')[:3]
    return render(request, 'web/Singlepage.html', {'icon': icon, 'relatedIcon': relatedIcon, 'relatedIconnotFound': relatedIconnotFound})
#
#END ICONS SINGLE VIEW


#START CATEGORIES SINGLE VIEW
#
#   SHOW LAST ICONS ADDED TO SPECIEFIED CATEGORIE ID
def categoriepage(request, categorie_id):
    categorie = get_object_or_404(CATEGORIES, id=categorie_id)

    return render(request, 'web/categoriepage.html', {'categorie': categorie})
#
#END CATEGORIES SINGLE VIEW


#START SEARCH RESULTS VIEW
#
#   SHOW USER SEARCH RESULTS ON SINGLE PAGE
def searchResults(request):
    iconsFound = ICON.objects.all()
    query = request.GET.get('searchQuery') #zakhire harchizi ke dar methode get amade ast
    searchResult = ICON.objects.filter(name__contains=query)
    #contains= Case-sensitive containment test. #fek konam yani hasas nist !!!
    return render(request, 'web/searchresults.html', {'searchResult': searchResult, 'query': query})
#
#START SEARCH RESULTS VIEW


#START ADMIN PAGE VIEW
#
#   SHOW USER SEARCH RESULTS ON SINGLE PAGE
def adminPage(request):
    allIcon = ICON.objects.all().order_by('-published_date')[:20]
    return render(request, 'web/adminpage.html', {'allIcon': allIcon})
#
#START ADMIN PAGE VIEW

class createIcon(CreateView):
    model= ICON
    fields= ['name','download_link','preview_image','categorie','copyright_title','copyright_link','views','published_date']
    success_url = reverse_lazy('index:index')

class updateIcon(UpdateView):
    model= ICON
    fields= ['name','download_link','preview_image','categorie','copyright_title','copyright_link','views', 'published_date']
    success_url = reverse_lazy('index:adminpage')

class deleteIcon(DeleteView):
    model= ICON
    success_url = reverse_lazy('index:adminpage')

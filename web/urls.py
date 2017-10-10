from django.conf.urls import url,include
from . import views

app_name= 'index'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^icon/(?P<thisicon_id>[0-9]+)/$', views.singlepage, name='singlepage'),
    url(r'^categorie/(?P<categorie_id>[0-9]+)/$', views.categoriepage, name='categoriepage'),
    url(r'^search/$', views.searchResults, name='searchresults'),
    url(r'^adminpage/$', views.adminPage, name='adminpage'),
    url(r'^icon/add/$', views.createIcon.as_view(), name='createIcon'),
    url(r'^icon/(?P<pk>[0-9]+)/update/$', views.updateIcon.as_view(), name='updateIcon'),
]

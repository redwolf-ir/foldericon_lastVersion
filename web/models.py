from django.db import models

#START CATEGORIE MODEL
#	#################
class CATEGORIES(models.Model):
	name= models.CharField(max_length= 100)

	def __str__(self):
		return self.name
#	#################
#END CATEGORIE MODEL


#START ICON MODEL
#	#################
class ICON(models.Model):
	name= models.CharField(max_length= 100)
	categorie= models.ForeignKey(CATEGORIES, on_delete= models.CASCADE)
	views= models.IntegerField(default=0)
	preview_image= models.FileField()
	download_link= models.CharField(max_length= 200)
	copyright_title= models.CharField(max_length= 50, verbose_name="copyright title link")
	copyright_link= models.CharField(max_length= 200, verbose_name="copy right link address")
	published_date= models.DateTimeField()

	def __str__(self):
		return self.name + ' - ' + str(self.categorie)
#	#################
#END ICON MODEL
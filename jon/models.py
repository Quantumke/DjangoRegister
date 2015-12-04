from django.db import models
from django.utils import timezone
# Create your models here.
class reg(models.Model):

	username = models.CharField(max_length=100, unique=True ,blank=False)
	email = models.EmailField(max_length=100, unique=True, blank=False)
	first_name= models.CharField(max_length=100, unique=False, blank=False)
	last_name = models.CharField(max_length=100, unique=False, blank=False)
	bio = models.TextField(max_length=100, unique=False, blank =False)
	profile_pic = models.CharField(max_length=100, unique=False, blank=False)
	web_url= models.URLField(max_length=100, unique=True, blank=False)
	date_created = models.DateField(timezone.now(), unique=False, blank=False)
	date_updated= models.DateField(timezone.now(), unique=False, blank=False)
	languages = models.CharField(max_length=100, unique=False, blank=True)
	slug = models.SlugField(max_length=100, unique=True, blank=False)

def dates(self):
	self.date_created = timezone.now()
	self.date_updated = timezone.now()
	self.save

def __str__(self):
	return self.username

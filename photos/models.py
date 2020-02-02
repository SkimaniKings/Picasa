from django.db import models
import datetime as dt

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/', default="")
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    location = models.ForeignKey('Location')
    category = models.ForeignKey('Category')
    
    def __str__(self):
        return self.description

   
class Category(models.Model):
    category = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category

class Location(models.Model):
    location = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location
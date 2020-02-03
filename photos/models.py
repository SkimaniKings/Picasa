from django.db import models
import datetime as dt

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField()
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    def search_by_location(cls,search_term):
        locate = cls.objects.filter(title__icontains=search_term)
        return locate

    def search_by_category(cls,search_term):
        locate = cls.objects.filter(title__icontains=search_term)
        return cate

   
class Category(models.Model):
    category = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category
    
    def search_by_category(cls,search_term):
        locate = cls.objects.filter(title__icontains=search_term)
        return locate

class Location(models.Model):
    location = models.CharField(max_length =30)
    
    
    
    
    def __str__(self):
        return self.location
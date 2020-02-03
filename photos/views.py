from django.shortcuts import render
from .models import Picture
from django.conf import settings


# Create your views here.

def home(request):
    images = Picture.objects.all()
    return render (request, 'home.html', {"images":images})

    



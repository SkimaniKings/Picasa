from django.shortcuts import render
from .models import Picture
from django.conf import settings


# Create your views here.

def home(request):
    images = Picture.objects.all()
    return render (request, 'home.html', {"images":images})

# def search_results(request):
    
#     if 'image' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_articles = Picture.search_by_category(search_term)
        
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})



def search_results(request):
    '''
    Method to search by location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images":searched_images})
    elif 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_location(search_term)
        message = f"{search_term}"    

        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})

def category(request, id):
    '''
    Method to search by images or category
    '''
    # categories = Category.get_all_categories()
    images = Image.objects.filter(category__id=id)
    context = {
        "categories":categories,
        "images":images
    }
    return render(request, 'category.html', context)





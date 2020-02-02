from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')


def search_results(request):
    
    if 'locate' in request.GET and request.GET["locate"]:
        search_term = request.GET.get("locate")
        searched_images = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"locate": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
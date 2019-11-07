from django.shortcuts import render

def index(request):
    """ A view that displays the index page """
    return render(request, "index.html")
    

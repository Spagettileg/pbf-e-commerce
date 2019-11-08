from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()  # Return all the products in the dbase  
    return render(request, "products.html", {"products": products})
    
    
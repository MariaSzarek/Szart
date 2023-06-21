from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    products = Product.objects.all
    return render(request, "Szart.html", {'items': products})

def item_response(request, id):
    products = get_object_or_404(Product, pk=id)
    return render(request, 'item.html', {'items': products})

def show_paintings(request):
    products = Product.objects.filter(type="0")
    return render(request, "paintings.html", {'items': products})

def show_ceramics(request):
    products = Product.objects.filter(type="1")
    return render(request, "ceramics.html", {'items': products})

def contact_response(request):
    return render(request, 'contact.html')

def aboutme_response(request):
    return render(request, 'aboutme.html')
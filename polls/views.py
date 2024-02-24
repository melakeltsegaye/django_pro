from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):

    products =  product.objects.all()
    data = {
        'product':products
    }
    return render(request, 'index.html', data)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    abou = aboutcont.objects.all()

    data = {
        'about': abou
    }


    return render(request, 'about.html', data)

def products(request):
    products =  product.objects.all()
    cata =  catagori.objects.all()
    data = {
        'product':products,
        'catagori':cata
    }
    return render(request, 'products.html', data)
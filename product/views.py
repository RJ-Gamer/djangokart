from django.shortcuts import render, redirect
from .models import Product
from django.utils.text import slugify
from django.contrib import messages
# Create your views here.
def product_list(request):
    products = Product.objects.active()
    context = {
        'products': products,
    }
    return render(request, 'product/product_list.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)

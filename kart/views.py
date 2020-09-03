from django.shortcuts import render, get_object_or_404
from .models import Basket, BasketLine
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.models import Product
from .forms import BasketLineFormset


# Create your views here.
def add_to_basket(request):
    product = get_object_or_404(Product, id = request.GET.get('product_id'))
    basket = request.basket

    if not request.basket:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        basket = Basket.objects.create(user=user)
        request.session['basket_id'] = basket.id

    basketline, created = BasketLine.objects.get_or_create(
        basket=basket, product=product
    )
    if not created:
        basketline.quantity += 1
        basketline.save()
    return HttpResponseRedirect(reverse('product:product_detail', args=(product.id, )))


def manage_basket(request):
    if not request.basket:
        return render(request, 'kart/basket.html', {'formset': None})

    if request.method == 'POST':
        formset = BasketLineFormset(request.POST, instance=request.basket)
        if formset.is_valid():
            formset.save()
    else:
        formset = BasketLineFormset(instance=request.basket)

    if request.basket.is_empty():
        return render(request, 'kart/basket.html', {'formset': None})
    return render(request, 'kart/basket.html', {'formset': formset})

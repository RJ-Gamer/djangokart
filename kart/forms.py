from django.forms import inlineformset_factory
from .models import Basket, BasketLine
from . import widgets
from django import forms
from user_address.models import Address

BasketLineFormset = inlineformset_factory(
    Basket,
    BasketLine,
    fields=('quantity',),
    extra=0,
    widgets={'quantity': widgets.PlusMinusNumberInputWidget()},
)

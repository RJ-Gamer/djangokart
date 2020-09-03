from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from . import forms
from django.urls import reverse_lazy
from django import forms as django_forms
from django.db import models as django_models
import django_filters
from django_filters.views import FilterView
from .models import Order

# Create your views here.
class AddressSelectionView(LoginRequiredMixin, FormView):
    template_name = 'order/address_select.html'
    form_class = forms.AddressSelectionForm
    success_url = reverse_lazy('order:checkout_done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        del self.request.session['basket_id']
        basket = self.request.basket
        basket.create_order(
            form.cleaned_data['billing_address'],
            form.cleaned_data['shipping_address']
        )
        return super().form_valid(form)

class DateInput(django_forms.DateInput):
    input_type = 'date'

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'user__email': ['icontains'],
            'status': ['exact'],
            'updated': ['gt', 'lt'],
            'created': ['gt', 'lt'],
        }
        filter_overrides = {
            django_models.DateTimeField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f:{
                    'widget': DateInput
                }
            }
        }

class OrderView(UserPassesTestMixin, FilterView):
    filterset_class = OrderFilter
    login_url = reverse_lazy('user:login')

    def test_func(self):
        return self.request.user.is_staff is True

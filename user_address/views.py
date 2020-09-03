from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from .models import Address
from django.views.generic import ListView

# Create your views here.
class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

class AddressCreateview(LoginRequiredMixin, CreateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('address:address_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('address:address_list')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('address:address_list')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

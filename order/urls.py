from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'order'
urlpatterns = [
    path('order/address_select/', views.AddressSelectionView.as_view(), name='address_select'),
    path('order/done/', TemplateView.as_view(template_name='order/order_done.html'), name='checkout_done'),
    path('order_dashboard/', views.OrderView.as_view(), name='order_dashboard'),
]

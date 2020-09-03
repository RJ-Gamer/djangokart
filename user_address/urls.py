from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('address/', views.AddressListView.as_view(), name='address_list'),
    path('address/create/', views.AddressCreateview.as_view(), name='address_create'),
    path('address/<int:pk>/', views.AddressUpdateView.as_view(), name='address_update'),
    path('address/<int:pk>/delete/', views.AddressDeleteView.as_view(), name='address_delete'),
]

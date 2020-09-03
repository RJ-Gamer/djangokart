from django.urls import path
from . import views


app_name = 'kart'

urlpatterns = [
    path('add_to_basket/', views.add_to_basket, name='add_to_basket'),
    path('basket/', views.manage_basket, name='basket'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view(), name='users'),
    path('users/<pk>', views.UserDetailAPIView.as_view(), name='user-detail'),
]

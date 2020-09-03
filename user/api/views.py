from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import UserSerializer
from user.models import User

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

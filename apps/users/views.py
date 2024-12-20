from rest_framework import generics
from .models import User
from apps.users.api.serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

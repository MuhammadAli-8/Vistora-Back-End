from django.contrib.auth import get_user_model
from rest_framework import viewsets
from apps.users.api.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and managing User instances.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put']

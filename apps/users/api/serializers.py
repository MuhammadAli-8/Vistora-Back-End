from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = ['id',  'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login',"groups","user_permissions",]
        exclude = ['password']

from rest_framework.serializers import ModelSerializer

from .models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone', 'address')
        read_only_fields = ('id',)

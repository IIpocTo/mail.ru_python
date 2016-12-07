from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from .models import UserProfile, Account


class UserSerializer(ModelSerializer):
    accounts = PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',  'phone', 'address', 'accounts')
        read_only_fields = ('id', 'username', 'password', 'email', 'phone')




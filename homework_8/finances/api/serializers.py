from rest_framework.serializers import ModelSerializer

from ..models import Account


class AccountListSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'user',
            'number'
        ]


class AccountDetailSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'user',
            'number'
        ]

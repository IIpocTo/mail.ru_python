from rest_framework.serializers import ModelSerializer

from ..models import Account, Charge


class AccountListSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'number'
        ]


class AccountDetailSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'user',
            'number'
        ]


class ChargeListSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = [
            'id',
            'account',
            'value',
            'date'
        ]


class ChargeDetailSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = [
            'account',
            'value',
            'date'
        ]

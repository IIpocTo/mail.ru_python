from rest_framework.serializers import ModelSerializer

from ..models import Account, Charge, UserProfile


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


class UserListSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'phone',
        ]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'address',
        ]


class StatisticSerializer(ModelSerializer):
    class Meta:
        model = Charge
        fields = [
            'year',
            'month',
            'total',
        ]

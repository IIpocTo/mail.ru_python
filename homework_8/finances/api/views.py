from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAccountOwner, IsChargeOwner
from .serializers import (
    AccountDetailSerializer, AccountListSerializer, ChargeListSerializer, ChargeDetailSerializer
)
from ..models import Account, Charge


class AccountList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class AccountDetail(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer
    lookup_field = 'number'
    permission_classes = [IsAccountOwner]


class ChargeList(ListCreateAPIView):
    queryset = Charge.objects.all()
    serializer_class = ChargeListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['account__number']

    # def perform_create(self, serializer):
    #     serializer.save(account=self.request.user__account)

    def get_queryset(self):
        return Charge.objects.filter(account__user=self.request.user)


class ChargeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Charge.objects.all()
    serializer_class = ChargeDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsChargeOwner]

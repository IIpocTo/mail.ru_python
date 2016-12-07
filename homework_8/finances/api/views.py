from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsOwnerOrReadOnly
from .serializers import AccountDetailSerializer, AccountListSerializer
from ..models import Account


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
    permission_classes = [IsOwnerOrReadOnly]

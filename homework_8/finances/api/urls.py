from django.conf.urls import url

from .views import AccountList, AccountDetail

urlpatterns = [
    url(r'^accounts/$', AccountList.as_view(), name='account_list'),
    url(r'^accounts/(?P<number>\d+)/$', AccountDetail.as_view(), name='account_detail')
]

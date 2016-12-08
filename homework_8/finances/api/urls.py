from django.conf.urls import url

from .views import AccountList, AccountDetail, ChargeList, ChargeDetail, StatisticsList

urlpatterns = [
    url(r'^accounts/$', AccountList.as_view(), name='account_list'),
    url(r'^accounts/(?P<number>\d+)/$', AccountDetail.as_view(), name='account_detail'),
    url(r'^charges/$', ChargeList.as_view(), name='charge_list'),
    url(r'^charges/(?P<id>\d+)/$', ChargeDetail.as_view(), name='charge_detail'),
    url(r'^accounts/(?P<number>\d+)/statistics$', StatisticsList.as_view(), name='statistics_list')
]

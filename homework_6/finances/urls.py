from django.conf.urls import url

from .views import MainPageView, AccountView, AddChargeView, AccountSearchView, AccountInsertView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^search/$', AccountSearchView.as_view(), name='search'),
    url(r'^insert/$', AccountInsertView.as_view(), name='insert'),
    url(r'^charges/(?P<number>\d+)/$', AccountView.as_view(), name='account'),
    url(r'^charges/(?P<number>\d+)/add/$', AddChargeView.as_view(), name='add_charge'),
]

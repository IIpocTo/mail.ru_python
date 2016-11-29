from django.conf.urls import url

from .views import MainPageView, AccountView, AddChargeView, AccountSearchView, AccountInsertView, AccountStatisticsView, LoginView, RegisterView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^search/$', AccountSearchView.as_view(), name='search'),
    url(r'^insert/$', AccountInsertView.as_view(), name='insert'),
    url(r'^charges/(?P<number>\d+)/$', AccountView.as_view(), name='account'),
    url(r'^charges/(?P<number>\d+)/add/$', AddChargeView.as_view(), name='add_charge'),
    url(r'^charges/(?P<number>\d+)/statistics/$', AccountStatisticsView.as_view(), name='statistics'),
    url(r'^register/$', RegisterView, name="register"),
    url(r'^login/$', LoginView, name="login"),
    url(r'^profile/$', AccountInsertView, name="profile")
]

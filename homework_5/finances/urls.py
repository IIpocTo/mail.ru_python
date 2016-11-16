from django.conf.urls import url

from .views import MainPageView, GeneratorView, ChargeView, AddChargeView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^charges/(?P<number>\d+)/$', ChargeView.as_view(), name='charge'),
    url(r'^charges/(?P<number>\d+)/add/$', AddChargeView.as_view(), name='add_charge'),
    url(r'^generator/$', GeneratorView.as_view(), name='generator')
]

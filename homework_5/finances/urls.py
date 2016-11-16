from django.conf.urls import url

from .views import MainPageView, GeneratorView, FinanceView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^charges/(?P<number>\d+)/$', FinanceView.as_view(), name='finances'),
    url(r'^generator/$', GeneratorView.as_view(), name='generator')
]

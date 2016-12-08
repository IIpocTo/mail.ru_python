from django.conf.urls import url

from .views import MainPageView, AccountAmountView, LoginView, LogoutView, RegisterView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^accounts/(?P<pk>\d+)/amount', AccountAmountView.as_view(), name='amount')
]

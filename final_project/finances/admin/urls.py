from django.conf.urls import url

from .views import (
    AdminMainView
)

urlpatterns = [
    url(r'^$', AdminMainView.as_view(), name='main'),
]
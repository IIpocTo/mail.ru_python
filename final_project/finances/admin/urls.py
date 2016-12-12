from django.conf.urls import url

from .views import (
    AdminMainView, AdminUserListView
)

urlpatterns = [
    url(r'^$', AdminMainView.as_view(), name='main'),
    url(r'^users/$', AdminUserListView.as_view(), name='user_list'),
]
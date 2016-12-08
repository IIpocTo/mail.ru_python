from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("finances.urls", namespace='finances')),
    url(r'^api/', include("finances.api.urls", namespace='api')),
    url(r'session_security/', include('session_security.urls'))
]

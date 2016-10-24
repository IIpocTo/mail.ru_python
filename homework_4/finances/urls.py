from django.conf.urls import url

from .views import main_page, finance_page, generator_page

urlpatterns = [
    url(r'^$', main_page, name='main'),
    url(r'^charges/$', finance_page, name='finances'),
    url(r'^generator/$', generator_page, name='generator')
]

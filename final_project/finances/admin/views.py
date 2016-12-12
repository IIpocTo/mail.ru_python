from django.views import generic
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from ..models import Account, Charge, UserProfile


class AdminMainView(generic.TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, self.template_name, {
                    "title": "Main page"
                })
        raise PermissionDenied
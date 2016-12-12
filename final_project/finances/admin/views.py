from django.views import generic
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


class AdminUserListView(generic.TemplateView):
    template_name = "user_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                user_list = UserProfile.objects.filter(is_staff=False)
                paginator = Paginator(user_list, 10)
                page_next = None
                page_previous = None
                page = request.GET.get('page')
                try:
                    users = paginator.page(page)
                    page_next = page - 1
                    page_previous = page + 1
                except PageNotAnInteger:
                    users = paginator.page(1)
                    page_next = 2
                    page_next = None
                except EmptyPage:
                    users = paginator.page(paginator.num_pages)
                    page_previous = paginator.num_pages - 1
                    page_next = None

                return render(request, self.template_name, {
                    'users': users,
                    'page_next': page_next,
                    'page_previous': page_previous
                })
        raise PermissionDenied

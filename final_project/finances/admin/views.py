from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.contrib import messages
import json
import requests

from ..models import Account, Charge, UserProfile
from .forms import UserEditForm, UserDeleteForm

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
    form_class = UserEditForm
    delete_form_class = UserDeleteForm

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
                    'page_previous': page_previous,
                    'form': self.form_class,
                    'delete_form': self.delete_form_class
                })
        raise PermissionDenied


class AdminEditUserView(generic.View):
    form_class = UserEditForm

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                form = self.form_class(request.POST)
                if form.is_valid():
                    headers = {'Authorization': 'JWT ' + request.session["token"]}
                    username=form.cleaned_data['username']
                    data = {
                        'first_name': form.cleaned_data['first_name'],
                        'last_name': form.cleaned_data['last_name'],
                        'email': form.cleaned_data['email'],
                        'address': form.cleaned_data['address'],
                        'phone': form.cleaned_data['phone'].country_code + form.cleaned_data['phone'].national_number,
                    }
                    put = requests.put("http://localhost:8000" + reverse("api:user_detail", args={username}),
                                       data=data,
                                       headers=headers
                                       )
                    if put.status_code == 200:
                        success_message = "You have updated user data!"
                        messages.success(request, success_message)
                    else:
                        error_message = "Something went wrong with the update :("
                        messages.error(request, error_message)
                    return redirect(reverse("admin:user_list"))
                else:
                    error_message = form.errors
                    messages.error(request, error_message)
                    return redirect(reverse("admin:user_list"))
        raise PermissionDenied


class AdminDeleteUserView(generic.View):
    form_class = UserDeleteForm

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                form = self.form_class(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get("username")
                    headers = {'Authorization': 'JWT ' + request.session["token"]}
                    delete = requests.delete("http://localhost:8000" + reverse("api:user_detail", args={username}),
                                             headers=headers
                                             )
                    if delete.status_code == 204:
                        success_message = "The user " + username + " has been deleted successfully!"
                        messages.success(request, success_message)
                    else:
                        error_message = "Something went wrong with the deleting"
                        messages.error(request, error_message)
                else:
                    error_message = form.errors
                    messages.error(request, error_message)
                return redirect(reverse("admin:user_list"))
        raise PermissionDenied


class AdminSearchUserView(generic.TemplateView):
    template_name = "user_detail.html"

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        headers = {'Authorization': 'JWT ' + request.session["token"]}
        get_user = requests.get(
            "http://localhost:8000" + reverse("api:user_list") + "?search=" + username,
            headers=headers
        )
        user = get_user.json()[0]
        headers = {'Authorization': 'JWT ' + request.session["token"]}
        response = requests.get("http://localhost:8000" + reverse("api:account_list") + "?search=" + username, headers=headers)
        accounts = json.loads(response.content.decode())
        return render(request, self.template_name, {
            "title": "User detail view",
            "user": user,
            "accounts": accounts
        })



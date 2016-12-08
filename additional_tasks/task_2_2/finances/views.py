from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm
from .models import Account


def is_owner(f):
    def wrapper(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        account = get_object_or_404(Account.objects.filter(id=pk))
        if account.owner == request.user.id:
            return f(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrapper


class MainPageView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Main Page"
        })


class RegisterView(generic.TemplateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Register",
            "form": self.form_class,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            User.objects.create_user(
                username=user_name,
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            success_message = "You have been registered"
            info_message = "You registered new User(" \
                           "login: " + str(user_name) \
                           + ")"
            messages.success(request, success_message)
            messages.info(request, info_message)

            return render(request, self.template_name, {
                "title": "Register",
                "form": self.form_class
            })
        return render(request, self.template_name, {
            "title": "Register",
            "form": form
        })


class LoginView(generic.TemplateView):
    template_name = 'auth.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Login",
            "form": self.form_class,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("finances:main"))
            else:
                messages.error(request, "Your login data is not valid")
                return render(request, self.template_name, {
                    "title": "Login",
                    "form": form
                })
        messages.error(request, "Incorrect data")
        return render(request, self.template_name, {
            "title": "Login",
            "form": form
        })


class LogoutView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect("finances:main")
        else:
            raise PermissionDenied


class AccountAmountView(generic.TemplateView):
    template_name = 'account.html'

    @is_owner
    def get(self, request, pk=None, *args, **kwargs):
        if request.user.is_authenticated:
            account = Account.objects.get(id=pk)
            return render(request, self.template_name, {
                "title": "Account Amount",
                "account": account
            })
        else:
            raise PermissionDenied


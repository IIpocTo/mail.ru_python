from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Sum
from django.db.models.functions import Extract
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .calendar import get_month_name
from .forms import ChargeForm, AccountForm, AccountLookForForm, RegisterForm, LoginForm, ProfileUpdateForm
from .models import Account, Charge, UserProfile


class MainPageView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Main Page",
        })


class RegisterView(generic.TemplateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Register",
            "form": self.form_class,
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['username']
            UserProfile.objects.create_user(
                username=user_name,
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("finances:profile"))
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
            return render(request, self.template_name, {
                "title": "Main page"
            })
        else:
            raise PermissionDenied


class ProfileUpdateView(generic.TemplateView):
    template_name = 'profile.html'
    form_update_class = ProfileUpdateForm
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def post(self, request, *args, **kwargs):
        form_update = self.form_update_class(request.POST)
        form = self.form_class
        form_look_for = self.form_look_for_class

        if form.is_valid():
            u = UserProfile.objects.get(username__exact='john')
            u.address = form.address
            u.save()
            return render(request, self.template_name, {
                "title": "Profile",
                "form": form,
                "form_update": form_update,
                "form_look_for": form_look_for
            })
        else:
            return render(request, self.template_name, {
                "title": "Profile",
                "form": form,
                "form_update": form_update,
                "form_look_for": form_look_for
            })


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
    form_update_class = ProfileUpdateForm
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            return render(request, self.template_name, {
                "title": "Profile",
                "form": self.form_class,
                "form_update": self.form_update_class,
                "form_look_for": self.form_look_for_class
            })
        else:
            raise PermissionDenied


class AccountInsertView(generic.TemplateView):
    template_name = 'profile.html'
    form_update_class = ProfileUpdateForm
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form_look_for = self.form_look_for_class
        form_update = self.form_update_class

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            success_message = "Form successfully validated!"
            info_message = "You created new Account(" \
                           "number: " + str(request.POST.get('number')) \
                           + ")"

            messages.success(request, success_message)
            messages.info(request, info_message)
            return HttpResponseRedirect(instance.get_absolute_url())

        return render(request, self.template_name, {
            "title": "Profile",
            "form": form,
            "form_update": form_update,
            "form_look_for": form_look_for
        })


class AccountSearchView(generic.TemplateView):
    template_name = 'profile.html'
    form_update_class = ProfileUpdateForm
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def post(self, request, *args, **kwargs):
        form_look_for = self.form_look_for_class(request.POST)
        form = self.form_class
        form_update = self.form_update_class

        if form_look_for.is_valid():
            return HttpResponseRedirect(reverse('finances:account', args=[request.POST.get('number')]))

        return render(request, self.template_name, {
            "title": "Profile",
            "form": form,
            "form_update": form_update,
            "form_look_for": form_look_for
        })


class AccountView(generic.FormView):
    template_name = "account.html"

    @transaction.atomic()
    def get(self, request, number=None, *args, **kwargs):
        if request.user.is_authenticated:
            account = get_object_or_404(Account, number=number)
            if account.user == request.user:
                deposit = Charge.objects.filter(account=account, value__gt=0.0).order_by('date')
                withdraw = Charge.objects.filter(account=account, value__lt=0.0).order_by('date')
                return render(request, self.template_name, {
                    "title": "Account page",
                    "deposit": deposit,
                    "withdraw": withdraw,
                    "account_number": account.number
                })
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied


class AddChargeView(generic.FormView):
    template_name = "add_charge.html"
    form_class = ChargeForm
    title_name = "Add new Charge"

    def get(self, request, number=None, *args, **kwargs):
        if request.user.is_authenticated:
            account = get_object_or_404(Account, number=number)
            if account.user == request.user:
                return render(request, self.template_name, {
                    "title": self.title_name,
                    "form": self.form_class,
                    "account_number": number
                })
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied

    def post(self, request, number=None, *args, **kwargs):
        get_object_or_404(Account, number=number)
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_id = number
            instance.save()
            success_message = "Form successfully validated!"
            info_message = "You created new Charge(" \
                           "value: " + str(request.POST.get('value')) + \
                           ", date: " + request.POST.get('date') + ")"

            messages.success(request, success_message)
            messages.info(request, info_message)
        return render(request, self.template_name, {
            "title": self.title_name,
            "form": form,
            "account_number": number
        })


class AccountStatisticsView(generic.FormView):
    template_name = "statistics.html"

    def get_my_data(self, variables, acc=None):
        if len(variables) == 0:
            return acc
        else:
            year, month, total = variables.pop(-1)
            if acc is None:
                acc = {year: {get_month_name(month): total}}
            else:
                if acc.get(year) is not None:
                    if get_month_name(month) not in acc[year]:
                        acc[year][get_month_name(month)] = total
                else:
                    acc[year] = {get_month_name(month): total}
            acc_new = self.get_my_data(variables, acc)
            return acc_new

    def get(self, request, number=None, *args, **kwargs):
        if request.user.is_authenticated:
            account = get_object_or_404(Account, number=number)
            if account.user == request.user:
                stats2 = (Charge.objects
                          .filter(account=account)
                          .annotate(month=Extract('date', 'month'))
                          .values('month')
                          .annotate(total=Sum('value'))
                          .annotate(year=Extract('date', 'year'))
                          .values('year', 'month', 'total')
                          .order_by('year', 'month')
                          .values_list('year', 'month', 'total'))
                stats = self.get_my_data(list(stats2))
                return render(request, self.template_name, {
                    "title": "Account Statistics",
                    "data": stats,
                    "account_number": number
                })
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied

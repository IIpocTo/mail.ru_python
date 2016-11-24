from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Sum
from django.db.models.functions import Extract
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .calendar import get_month_name
from .forms import ChargeForm, AccountForm, AccountLookForForm
from .models import Account, Charge


class MainPageView(generic.TemplateView):
    template_name = 'main.html'
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Main Page",
            "form": self.form_class,
            "form_look_for": self.form_look_for_class
        })


class AccountInsertView(generic.TemplateView):
    template_name = 'main.html'
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form_look_for = self.form_look_for_class

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
            "title": "Finances",
            "form": form,
            "form_look_for": form_look_for
        })


class AccountSearchView(generic.TemplateView):
    template_name = 'main.html'
    form_class = AccountForm
    form_look_for_class = AccountLookForForm

    def post(self, request, *args, **kwargs):
        form_look_for = self.form_look_for_class(request.POST)
        form = self.form_class

        if form_look_for.is_valid():
            return HttpResponseRedirect(reverse('finances:account', args=[request.POST.get('number')]))

        return render(request, self.template_name, {
            "title": "Finances",
            "form": form,
            "form_look_for": form_look_for
        })


class AccountView(generic.FormView):
    template_name = "account.html"

    @transaction.atomic()
    def get(self, request, number=None, *args, **kwargs):
        account = get_object_or_404(Account, number=number)
        deposit = Charge.objects.filter(account=account, value__gt=0.0).order_by('date')
        withdraw = Charge.objects.filter(account=account, value__lt=0.0).order_by('date')
        return render(request, self.template_name, {
            "title": "Account page",
            "deposit": deposit,
            "withdraw": withdraw,
            "account_number": account.number
        })


class AddChargeView(generic.FormView):
    template_name = "add_charge.html"
    form_class = ChargeForm
    title_name = "Add new Charge"

    def get(self, request, number=None, *args, **kwargs):
        get_object_or_404(Account, number=number)
        return render(request, self.template_name, {
            "title": self.title_name,
            "form": self.form_class,
            "account_number": number
        })

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
            a, b, c = variables.pop(-1)
            if acc is None:
                acc = {a: {get_month_name(b): c}}
            else:
                if acc.get(a) is not None:
                    if get_month_name(b) not in acc[a]:
                        acc[a][get_month_name(b)] = c
                else:
                    acc[a] = {get_month_name(b): c}
            acc_new = self.get_my_data(variables, acc)
            return acc_new

    def get(self, request, number=None, *args, **kwargs):
        account = get_object_or_404(Account, number=number)
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

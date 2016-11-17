from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Account, Charge
from .forms import ChargeForm, AccountForm, AccountLookForForm, ChargeGoToForm


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
    template_name = "charge.html"
    form_class = ChargeGoToForm

    def get(self, request, number=None, *args, **kwargs):
        form = self.form_class
        account = get_object_or_404(Account, number=number)
        deposit = Charge.objects.filter(account=account, value__gt=0.0).order_by('date')
        withdraw = Charge.objects.filter(account=account, value__lt=0.0).order_by('date')
        return render(request, self.template_name, {
            "title": "Add charge",
            "deposit": deposit,
            "withdraw": withdraw,
            "account_number": account.number,
            "form": form
        })

    def post(self, request, number=None, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('finances:add_charge', args=[number]))
        account = get_object_or_404(Account, number=number)
        deposit = Charge.objects.filter(account=account, value__gt=0.0).order_by('date')
        withdraw = Charge.objects.filter(account=account, value__lt=0.0).order_by('date')
        return render(
            request, self.template_name, {
                "title": "Add charge",
                "deposit": deposit,
                "withdraw": withdraw,
                "account_number": account.number,
                "form": form
            }
        )


class AddChargeView(generic.FormView):
    template_name = "add_charge.html"
    form_class = ChargeForm
    title_name = "Your charges"

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
            # return HttpResponseRedirect(instance.get_absolute_url())
        return render(request, self.template_name, {
            "title": self.title_name,
            "form": form,
            "account_number": number
        })

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import ChargeForm
from .generator import random_transactions


class MainPageView(generic.TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Main Page"})


class FinanceView(generic.FormView):
    template_name = "finances.html"
    form_class = ChargeForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "title": "Finances",
            "form": self.form_class
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            success_message = "Form successfully validated!"
            info_message = "You created new Charge(" \
                           "value: " + str(request.POST.get('value')) + \
                           ", date: " + request.POST.get('date') + ")"

            messages.success(request, success_message)
            messages.info(request, info_message)
            return HttpResponseRedirect(instance.get_absolute_url())

        return render(request, self.template_name, {
            "title": "Finances",
            "form": form
        })


class GeneratorView(generic.TemplateView):
    template_name = 'generator.html'

    def get(self, request, *args, **kwargs):
        deposit = []
        withdraw = []

        for (date, value) in random_transactions():
            if value < 0:
                withdraw.append((date, value))
            else:
                deposit.append((date, value))

        return render(request, self.template_name, {
            "title": "Generator",
            "deposit": deposit,
            "withdraw": withdraw
        })

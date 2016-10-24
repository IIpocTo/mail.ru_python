from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ChargeForm
from .generator import random_transactions


def main_page(request):
    context = {
        "title": "Main Page"
    }
    return render(request, "main.html", context)


def finance_page(request):
    form = ChargeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        success_message = "Successfully created new Charge(value: " + str(
            request.POST.get('value')) + ", date: " + request.POST.get('date') + ")"
        messages.success(request, success_message)
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Finances",
        "form": form
    }
    return render(request, "finances.html", context)


def generator_page(request):
    deposit = []
    withdraw = []
    for (date, value) in random_transactions():
        if value < 0:
            withdraw.append((date, value))
        else:
            deposit.append((date, value))
    context = {
        "title": "Generator",
        "deposit": deposit,
        "withdraw": withdraw
    }
    return render(request, "generator.html", context)

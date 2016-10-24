from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ChargeForm


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

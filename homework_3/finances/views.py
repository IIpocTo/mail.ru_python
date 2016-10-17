from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader

from .models import Charge


def main_page(request):
    template = loader.get_template("main.html")
    context = RequestContext(request, {
        "title": "Main Page"
    })
    return HttpResponse(template.render(context))


def finance_page(request):
    queryset = Charge.objects.all()
    template = loader.get_template("finances.html")
    context = RequestContext(request, {
        "object_list": queryset,
        "title": "Finances"
    })
    return HttpResponse(template.render(context))

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


def index(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)


class IndexView(TemplateView):
    template_name = "index.html"
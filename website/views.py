from django.shortcuts import render
from . import models
from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = "index.html"

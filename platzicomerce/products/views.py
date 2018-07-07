from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TestView(TemplateView):
    template_name = "products/test.html"



class HomeView(TemplateView):
    template_name = "products/index.html"


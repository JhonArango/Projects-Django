from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import EjercicioGuia

# Create your views here.


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self,*args,**kwargs):
        ejercicios = EjercicioGuia.objects.all()
        return {'ejercicios':ejercicios}
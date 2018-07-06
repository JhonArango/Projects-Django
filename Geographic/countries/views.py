from django.shortcuts import render
from django.http import HttpResponse
from countries.models import Country
from django.views.generic import TemplateView
from django.views.generic.list import ListView

# Create your views here.
class CountrySearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        query = self.kwargs['query']
        return Country.objects.filter(continent__name=query)

class HomeView(TemplateView):
    template_name = "countries/home.html"

class CountryDetailView(TemplateView):
    template_name = "countries/country_detail.html"

    def get_context_data(self,*args,**kwargs):
        code = kwargs['code']
        return {'code':code}
    
#Esta parte ya no se hace necesario porque estamos usando un context_processor para todos los html
    # def get_context_data(self,*args,**kwargs):
    #     Colombia = {'name':'Colombia','code':'CO'}
    #     Peru = {'name':'Peru','code':'PE'}
    #     Usa = {'name':'Usa','code':'USA'}
    #     Argentina = {'name':'Argentina','code':'ARG'}

    #     countries = [Colombia,Peru,Usa,Argentina]
    #     return {'countries':countries}

class TagsView(TemplateView):
    template_name = "countries/Tags.html"

   
    
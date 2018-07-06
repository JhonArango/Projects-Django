from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Continent

# Create your views here.
class ContinentView(TemplateView):
    template_name = "continents/continents.html"

class ContinentDetailView(DetailView):
    template_name = "continents/continent_detail.html"
    model = Continent


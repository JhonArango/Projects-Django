from django.views.generic import TemplateView

# Create your views here.
class ContinentView(TemplateView):
    template_name = "continents/continents.html"
from countries.models import Country
from continents.models import Continent

def countries_data(request):
    countries = Country.objects.all()
    return {'countries':countries}


def continents_data(request):
    continents = Continent.objects.all()
    return {'continents':continents}
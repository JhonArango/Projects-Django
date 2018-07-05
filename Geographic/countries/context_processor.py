from countries.models import Country

def countries_data(request):
    countries = Country.objects.all()
    return {'countries':countries}


def continents_data(request):
    America = {'name':'America','color':'Rojo'}
    Europa = {'name':'Europa','color':'Azul'}
    Asia = {'name':'Asia','color':'Amarillo'}
    Africa = {'name':'Africa','color':'Negro'}
    Oceania = {'name':'Oceania','color':'Verde'}

    continents = [America,Europa,Asia,Africa,Oceania]
    return {'continents':continents}
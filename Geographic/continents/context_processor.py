def countries_data(request):
    Colombia = {'name':'Colombia','code':'CO'}
    Peru = {'name':'Peru','code':'PE'}
    Usa = {'name':'Usa','code':'USA'}
    Argentina = {'name':'Argentina','code':'ARG'}

    countries = [Colombia,Peru,Usa,Argentina]
    return {'countries':countries}
    
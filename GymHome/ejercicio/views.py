from django.shortcuts import render

# Create your views here.
def ejercicios(request):
    
    return render(request,"ejercicio/ejercicios.html")

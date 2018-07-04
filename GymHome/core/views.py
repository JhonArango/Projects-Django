from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def suplementacion(request):
    return render(request,"core/suplementacion.html")
    
def rutina(request):
    return render(request,"core/rutina.html")
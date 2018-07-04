from django.urls import path
from ejercicio import views as core_ejercicio


urlpatterns = [
    path('',core_ejercicio.ejercicios,name="ejercicios"),
]

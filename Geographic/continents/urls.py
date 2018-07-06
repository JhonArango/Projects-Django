from django.urls import path
from continents.views import ContinentView,ContinentDetailView

urlpatterns = [
    path('',ContinentView.as_view(),name="continents"),
    path('continent/<int:pk>/',ContinentDetailView.as_view(),name="continent_detail"),

]

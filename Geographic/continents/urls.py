from django.urls import path
from continents.views import ContinentView

urlpatterns = [
    path('',ContinentView.as_view(),name="continents"),
]

from django.urls import path
from countries.views import HomeView,TagsView,CountryDetailView,CountrySearchView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('tags/',TagsView.as_view(),name="tags"),
    path('search/<query>',CountrySearchView.as_view(),name="country_search"),
    path('countries/<code>',CountryDetailView.as_view(),name="countries_detail"),



]

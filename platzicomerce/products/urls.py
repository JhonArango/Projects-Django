from django.urls import path
from products.views import TestView,HomeView

urlpatterns = [
    path('test/',TestView.as_view(),name="test"),
    path('',HomeView.as_view(),name="home"),
]

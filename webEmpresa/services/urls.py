from django.urls import path
from . import views as services_views


urlpatterns = [
    # paths del core
    path('',services_views.services, name="services"),
]

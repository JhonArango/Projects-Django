from django.urls import path
from .views import SignView,ProfileUpdate

urlpatterns = [

    path('signup/',SignView.as_view(),name='signup'),
    path('profile/',ProfileUpdate.as_view(),name='profile'),
]

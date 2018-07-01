from django.urls import path
from .views import PageListView,PageDetailView

profiles_patterns = ([
    path('', PageListView.as_view(), name='list'),
    path('<username>/', PageDetailView.as_view(), name='detail'),  
],'profiles')
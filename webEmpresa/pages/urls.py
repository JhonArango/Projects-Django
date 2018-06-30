from django.urls import path
from . import views as pages_views


urlpatterns = [
    # paths del core
     path('<int:page_id>/<slug:page_title>/',pages_views.page,name="page")
]

  
 
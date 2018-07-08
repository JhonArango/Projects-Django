from django.urls import path
from products.views import TestView,HomeView,ProductoDetailView,ProductBuyView

urlpatterns = [
    path('test/',TestView.as_view(),name="test"),
    path('',HomeView.as_view(),name="home"),
    path('products/<slug:slug>/',ProductoDetailView.as_view(),name="product_detail"),
    path('products/<slug:slug>/buy/',ProductBuyView.as_view(),name="buy"),

]

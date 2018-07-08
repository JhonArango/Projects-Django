from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('comments/',include('comments.urls',namespace="comments")),
    path('accounts/',include('accounts.urls',namespace="accounts")),

] 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
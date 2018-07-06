from django.contrib import admin
from .models import Continent

# Register your models here.
class ContinentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Continent,ContinentAdmin)
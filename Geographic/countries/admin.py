from django.contrib import admin
from .models import Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country,CountryAdmin)
from django.contrib import admin
from core.models import EjercicioGuia

# Register your models here.
class EjercicioGuiaAdmin(admin.ModelAdmin):
    '''Admin View for '''
    readonly_fields = ('created','updated')


admin.site.register(EjercicioGuia,EjercicioGuiaAdmin)

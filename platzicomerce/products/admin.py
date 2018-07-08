from django.contrib import admin
from products.models import Product,ProduCategory,ProducImage

# Register your models here.
class ProducImageInLine(admin.TabularInline):
    model = ProducImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ProducImageInLine
    ]

admin.site.register(Product, ProductAdmin)

class ProduCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProduCategory, ProduCategoryAdmin)

class ProducImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProducImage, ProducImageAdmin)


from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","description","price","image_url","quantity")
admin.site.register(Product,ProductAdmin)

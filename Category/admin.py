from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("recyclable", "organic")

admin.site.register(Category, CategoryAdmin)


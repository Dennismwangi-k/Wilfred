from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display=("address","created_at","updated_at")
admin.site.register(Location,LocationAdmin)    



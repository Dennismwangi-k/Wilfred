from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('arrival_date', 'location', 'status')
admin.site.register(Delivery,DeliveryAdmin)    



# Register your models here.

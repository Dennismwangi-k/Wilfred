from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):     
    list_display = ('quantity','price', 'total_amount', 'order_status')

admin.site.register(Order, OrderAdmin)

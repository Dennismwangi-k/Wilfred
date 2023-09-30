from django.contrib import admin
from .models import OrderItem

class OrderItemAdmin(admin.ModelAdmin):
    list_display=("quantity","total_amount")
admin.site.register(OrderItem,OrderItemAdmin)    

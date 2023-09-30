from django.db import models
from django.db.models import F

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
    ]
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Dispatch')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, unique=True)


def total_price(self, quantity, item_price, delivery_rate):
    total_amount = quantity * (item_price + delivery_rate)
    return total_amount



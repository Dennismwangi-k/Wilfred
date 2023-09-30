from django.db import models

class OrderItem(models.Model):
    # order= models.ForeignKey('Order', on_delete=models.CASCADE)
    # product= models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.orderItem
    
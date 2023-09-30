from django.test import TestCase
from .models import Order
class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order(
            product_name="Plastic Waste ",
            price="50.00",
            quantity=3,
            order="Sample Order",
        )
    def test_order_creation(self):
        self.assertEqual(self.order.product_name, "Plastic Waste")
        self.assertEqual(self.order.price, "50.00")
        self.assertEqual(self.order.quantity, 3)
        self.assertEqual(self.order.order, "Sample Order")
    def test_order_str_method(self):
       self.assertEqual(str(self.order), "Sample Order")
    def test_order_defaults(self):
        default_order = Order.objects.create(product_name="Default Product", price="25.00")
        self.assertEqual(default_order.quantity, 0) 
        self.assertEqual(default_order.order, "")  
    def test_order_save(self):
        self.order.save()
        saved_order = Order.objects.get(pk=self.order.pk)
        self.assertEqual(saved_order.product_name, "Plastic Waste")
    def test_order_delete(self):
        self.order.save()
        self.order.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(pk=self.order.pk)

from django.test import TestCase
from .models import Order

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            waste_type='Plastic',
            delivery_location='Nairobi',
            total_amount=100.00,
            quantity=5.0,
        )

    def test_order_creation(self):
        self.assertEqual(self.order.waste_type, 'Plastic')
        self.assertEqual(self.order.delivery_location, 'Nairobi')
        self.assertEqual(float(self.order.total_amount), 100.00)
        self.assertEqual(float(self.order.quantity), 5.0)

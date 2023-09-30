from django.test import TestCase
from .models import OrderItem

class OrderItemModelTestCase(TestCase):
    def setUp(self):
        self.order_item = OrderItem.objects.create(
            orderItem='Item A',
            quantity=5,
            total_amount=10.99
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.orderItem, 'Item A')
        self.assertEqual(self.order_item.quantity, 5)
        self.assertEqual(self.order_item.amount, 10.99)

    def test_order_item_string_representation(self):
        self.assertEqual(str(self.order_item), 'Item A')

    def test_order_item_quantity_positive_value(self):
        self.assertGreater(self.order_item.quantity, 0)

    def test_order_item_total_amount_decimal_places(self):
        decimal_places = OrderItem._meta.get_field('total_amount').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_order_item_total_amount_max_digits(self):
        max_digits = OrderItem._meta.get_field('total_amount').max_digits
        self.assertGreater(max_digits, 0)

    def test_order_item_str_representation_limit(self):
        max_length = OrderItem._meta.get_field('orderItem').max_length
        self.assertLessEqual(len(str(self.order_item)), max_length)
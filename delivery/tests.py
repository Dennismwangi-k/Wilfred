from django.test import TestCase
from datetime import date
from .models import Delivery

class DeliveryModelTestCase(TestCase):
    def setUp(self):
        self.delivery = Delivery.objects.create(
            company_name='ABC Company',
            arrival_date=date.today(),
            location='Some Location',
            status='pending'
        )

    def test_delivery_creation(self):
        self.assertEqual(self.delivery.company_name, 'ABC Company')
        self.assertEqual(self.delivery.arrival_date, date.today())
        self.assertEqual(self.delivery.location, 'Some Location')
        self.assertEqual(self.delivery.status, 'pending')

    def test_delivery_string_representation(self):
        self.assertEqual(str(self.delivery), 'ABC Company')

    def test_delivery_status_choices(self):
        choices = dict(Delivery.ORDER_STATUS_CHOICES)
        self.assertDictEqual(
            choices,
            {
                'pending': 'Pending',
                'dispatch': 'In Transit',
                'delivered': 'Delivered',
                'cancelled': 'Cancelled'
            }
        )

    def test_delivery_status_default_value(self):
        new_delivery = Delivery.objects.create(
            company_name='XYZ Company',
            arrival_date=date.today(),
            location='Another Location'
        )
        self.assertEqual(new_delivery.status, 'pending')

    def test_delivery_status_choices_limit(self):
        max_length = Delivery._meta.get_field('status').max_length
        self.assertLessEqual(len('dispatch'), max_length)
        self.assertLessEqual(len('delivered'), max_length)
        self.assertLessEqual(len('cancelled'), max_length)

    def test_delivery_str_representation_limit(self):
        max_length = Delivery._meta.get_field('company_name').max_length
        self.assertLessEqual(len(str(self.delivery)), max_length)
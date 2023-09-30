from django.test import TestCase
from datetime import datetime
from .models import Location

class LocationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            address="123 Main St, City, State"
        )

    def test_address_field(self):
        self.assertEqual(self.location.address, "123 Main St, City, State")

    def test_created_at_field(self):
        self.assertIsInstance(self.location.created_at, datetime)

    def test_updated_at_field(self):
        self.assertIsInstance(self.location.updated_at, datetime)

    def test_str_method(self):
        expected_str = "123 Main St, City, State"
        self.assertEqual(str(self.location), expected_str)
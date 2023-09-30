from django.test import TestCase
from .models import Product, Category

class CategoryModelTest(TestCase):
    def test_recyclable_choices(self):
        category = Category.objects.create(recyclable="glass")
        recyclable_choices = [choice[0] for choice in Category.RECYCLABLE_CHOICES]
        self.assertIn(category.recyclable, recyclable_choices)

    def test_organic_choices(self):
        category = Category.objects.create(organic="food_waste")
        organic_choices = [choice[0] for choice in Category.ORGANIC_CHOICES]
        self.assertIn(category.organic, organic_choices)

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(recyclable="glass", organic="food_waste")
        Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=19.99,
            image_url="test_image.jpg",
            quantity=10,
            category=category,
        )

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field("price").max_digits
        self.assertEquals(max_digits, 10)

    def test_price_decimal_places(self):
        product = Product.objects.get(id=1)
        decimal_places = product._meta.get_field("price").decimal_places
        self.assertEquals(decimal_places, 2)

    def test_quantity(self):
        product = Product.objects.get(id=1)
        quantity = product.quantity
        self.assertEquals(quantity, 10)

    def test_image_url_upload_to(self):
        product = Product.objects.get(id=1)
        upload_to = product._meta.get_field("image_url").upload_to
        self.assertEquals(upload_to, "uploads/")

    def test_category_relation(self):
        product = Product.objects.get(id=1)
        category = product.category
        self.assertIsNotNone(category)

    def test_company_name_default(self):
        product = Product.objects.get(id=1)
        company_name = product.company_name
        self.assertEquals(company_name, "")



        


from django.test import TestCase
from .models import Message

class MessageModelTest(TestCase):
    def setUp(self):
        self.message = Message.objects.create(
            sender='John',
            body='Hello, Jane! How are you?'
        )

    def test_message_str_representation(self):
        message_str = str(self.message)
        expected_str = f"Message {self.message.sender}"
        self.assertEqual(message_str, expected_str)

    def test_message_default_is_read_value(self):
        is_read = self.message.is_read
        self.assertFalse(is_read)

    def test_message_body(self):
        body = self.message.body
        self.assertEqual(body, 'Hello, Jane! How are you?')

    def test_message_timestamp_auto_now_add(self):
        timestamp = self.message.timestamp
        self.assertIsNotNone(timestamp)
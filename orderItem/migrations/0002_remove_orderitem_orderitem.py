# Generated by Django 4.2.4 on 2023-09-26 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='orderItem',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('dispatched', 'Dispatched'), ('delivered', 'Delivered')], default='Dispatch', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2025-01-19 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_delivery_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]

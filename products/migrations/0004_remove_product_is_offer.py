# Generated by Django 4.0.10 on 2023-10-14 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_offer',
        ),
    ]

# Generated by Django 4.0.10 on 2023-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_is_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_offer',
            field=models.BooleanField(default=False),
        ),
    ]
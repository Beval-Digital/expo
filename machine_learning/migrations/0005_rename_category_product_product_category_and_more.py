# Generated by Django 5.0.4 on 2024-06-04 11:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("machine_learning", "0004_customer_customer_type_customer_gender_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="category",
            new_name="product_category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="price",
            new_name="unit_price",
        ),
    ]

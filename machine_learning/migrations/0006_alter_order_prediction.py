# Generated by Django 5.0.4 on 2024-06-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("machine_learning", "0005_rename_category_product_product_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="prediction",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

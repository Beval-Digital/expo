# Generated by Django 5.0.4 on 2024-06-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("machine_learning", "0007_order_satisfaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="satisfaction",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("online_store", "0002_product_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="user",
        ),
    ]
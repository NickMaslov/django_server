# Generated by Django 4.1.5 on 2023-01-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_store", "0008_product_createdat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="createdAt",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

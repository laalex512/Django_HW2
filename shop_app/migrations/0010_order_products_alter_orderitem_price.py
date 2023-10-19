# Generated by Django 4.2.5 on 2023-10-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop_app", "0009_alter_client_register_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="shop_app.OrderItem", to="shop_app.product"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

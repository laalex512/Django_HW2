# Generated by Django 4.2.5 on 2023-10-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop_app", "0008_alter_product_added_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="register_date",
            field=models.DateTimeField(),
        ),
    ]
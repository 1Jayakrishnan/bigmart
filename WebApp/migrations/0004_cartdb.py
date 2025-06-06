# Generated by Django 5.1.3 on 2024-12-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WebApp", "0003_userdb"),
    ]

    operations = [
        migrations.CreateModel(
            name="CartDb",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Username", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "ProductName",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Quantity", models.IntegerField(blank=True, null=True)),
                ("Price", models.IntegerField(blank=True, null=True)),
                ("TotalPrice", models.IntegerField(blank=True, null=True)),
                (
                    "Image",
                    models.ImageField(blank=True, null=True, upload_to="Cart Images"),
                ),
            ],
        ),
    ]

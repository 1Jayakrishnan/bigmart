# Generated by Django 5.1.3 on 2024-11-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminApp", "0002_prodb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catdb",
            name="Description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

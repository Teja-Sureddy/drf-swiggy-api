# Generated by Django 4.1.6 on 2023-02-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="image",
            field=models.ImageField(upload_to="menu"),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="image",
            field=models.ImageField(upload_to="restaurant"),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clairvoyance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="majorarcana",
            name="card_image",
            field=models.ImageField(upload_to="MajorArcanaCards"),
        ),
    ]

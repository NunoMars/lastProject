# Generated by Django 3.2.4 on 2021-06-22 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clairvoyance", "0002_alter_majorarcana_card_image"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="sorted_card",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="clairvoyance.majorarcana",
            ),
        ),
    ]

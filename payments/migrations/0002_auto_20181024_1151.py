# Generated by Django 1.11.16 on 2018-10-24 09:51

import django.db.models.deletion
from django.db import migrations, models

import payments.utils


class Migration(migrations.Migration):
    dependencies = [("payments", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="details",
            field=payments.utils.JSONField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name="payment",
            name="extra",
            field=payments.utils.JSONField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name="payment",
            name="repeat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payments.Payment",
            ),
        ),
    ]

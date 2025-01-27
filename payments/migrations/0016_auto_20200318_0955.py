# Generated by Django 3.0.4 on 2020-03-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0015_payment_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="state",
            field=models.IntegerField(
                choices=[
                    (1, "New payment"),
                    (2, "Awaiting payment"),
                    (3, "Payment rejected"),
                    (4, "Payment accepted"),
                    (5, "Payment processed"),
                ],
                db_index=True,
                default=1,
            ),
        ),
    ]

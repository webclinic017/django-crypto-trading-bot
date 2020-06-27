# Generated by Django 3.0.5 on 2020-06-27 11:17

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trading_bot", "0010_auto_20200624_0905"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="default_fee_rate",
            field=models.DecimalField(
                decimal_places=4,
                default=Decimal(
                    "0.01000000000000000020816681711721685132943093776702880859375"
                ),
                max_digits=30,
            ),
        ),
        migrations.AlterField(
            model_name="ordererrorlog",
            name="error_type",
            field=models.CharField(
                choices=[
                    ("Insufficient Funds", "Insufficient Funds"),
                    ("Invalid Order", "Invalidorder"),
                ],
                max_length=50,
            ),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-30 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prices", "0003_remove_price_expiredate_price_creationdate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="expireDate",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 11, 6, 17, 57, 12, 119772, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Usersapp", "0008_remove_profile_coins"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="accountMoney",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
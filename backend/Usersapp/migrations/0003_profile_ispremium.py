# Generated by Django 4.1.5 on 2023-08-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Usersapp", "0002_rename_numberofgaims_profile_numberofgames"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="isPremium",
            field=models.BooleanField(default=False),
        ),
    ]

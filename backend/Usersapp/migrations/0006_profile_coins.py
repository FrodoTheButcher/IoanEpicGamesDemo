# Generated by Django 4.2.6 on 2023-10-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Usersapp", "0005_remove_profile_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="coins",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

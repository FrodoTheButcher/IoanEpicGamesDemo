# Generated by Django 4.2.6 on 2023-10-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prices", "0002_remove_price_expire_price_expiredate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="expireDate",
        ),
        migrations.AddField(
            model_name="price",
            name="creationDate",
            field=models.DateTimeField(auto_now_add=True, default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="price",
            name="id",
            field=models.IntegerField(
                auto_created=True, default=0, primary_key=True, serialize=False
            ),
        ),
    ]

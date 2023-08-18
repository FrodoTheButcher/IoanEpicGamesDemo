# Generated by Django 4.1.5 on 2023-08-18 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Gamesapp", "0003_game_introductionvideo"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.FloatField()),
                ("expireDate", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name="game",
            old_name="minimumPlayableAge",
            new_name="age",
        ),
        migrations.RemoveField(
            model_name="game",
            name="isFree",
        ),
        migrations.RemoveField(
            model_name="game",
            name="isPremium",
        ),
        migrations.AddField(
            model_name="game",
            name="sale",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="Gamesapp.gamesale",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="tags",
            field=models.ManyToManyField(to="Gamesapp.tag"),
        ),
    ]

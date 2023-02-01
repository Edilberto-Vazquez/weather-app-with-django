# Generated by Django 4.1.5 on 2023-02-01 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherStation",
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
                (
                    "location",
                    models.CharField(max_length=50, verbose_name="place of operation"),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                (
                    "init_upload_date",
                    models.DateTimeField(verbose_name="initial upload date"),
                ),
                (
                    "last_upload_date",
                    models.DateTimeField(verbose_name="last upload date"),
                ),
                ("active", models.BooleanField(verbose_name="station is active")),
                ("name", models.CharField(max_length=50, verbose_name="station name")),
            ],
        ),
        migrations.CreateModel(
            name="WeatherRecord",
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
                ("temp", models.FloatField(verbose_name="temperature")),
                ("chill", models.FloatField(verbose_name="thermal sensation")),
                ("dew", models.FloatField(verbose_name="dew point")),
                ("heat", models.FloatField(verbose_name="heat")),
                ("hum", models.FloatField(verbose_name="humidity")),
                ("bar", models.FloatField(verbose_name="atmospheric pressure")),
                ("rain", models.FloatField(verbose_name="rain")),
                ("record_date", models.DateTimeField(verbose_name="registration date")),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analysis.weatherstation",
                    ),
                ),
            ],
        ),
    ]

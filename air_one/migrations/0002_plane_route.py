# Generated by Django 4.1.5 on 2023-01-23 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("air_one", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plane",
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
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Plane number"
                    ),
                ),
                (
                    "travel_time",
                    models.PositiveSmallIntegerField(verbose_name="Travel time"),
                ),
                (
                    "from_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_city_set",
                        to="air_one.city",
                        verbose_name="departures from",
                    ),
                ),
                (
                    "to_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_city_set",
                        to="air_one.city",
                        verbose_name="arrives in",
                    ),
                ),
            ],
            options={
                "ordering": ["travel_time"],
            },
        ),
        migrations.CreateModel(
            name="Route",
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
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Route name"
                    ),
                ),
                (
                    "travel_times",
                    models.PositiveSmallIntegerField(verbose_name="Travel Time"),
                ),
                (
                    "from_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="route_from_city_set",
                        to="air_one.city",
                        verbose_name="Departing from a city",
                    ),
                ),
                (
                    "planes",
                    models.ManyToManyField(
                        to="air_one.plane", verbose_name="List of Planes"
                    ),
                ),
                (
                    "to_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="route_to_city_set",
                        to="air_one.city",
                        verbose_name="Arriving in a city",
                    ),
                ),
            ],
            options={
                "ordering": ["travel_times"],
            },
        ),
    ]

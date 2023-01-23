from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="City")

    class Meta:
        # verbose_name = "City"
        # verbose_name_plural = "Cities"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("cities:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Plane(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Plane number")
    travel_time = models.PositiveSmallIntegerField(verbose_name="Travel time")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        # null=True, blank=True,
        related_name="from_city_set",
        verbose_name="departures from",
    )
    to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="to_city_set",
        verbose_name="arrives in",
    )

    def __str__(self):
        return f"Plane № {self.name}  {self.from_city} to {self.to_city}"

    class Meta:
        # verbose_name = 'Plane'
        # verbose_name_plural = 'Planes'
        ordering = ["travel_time"]

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Departing and arrival cities are the same")
        qs = Plane.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Change travel time")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Route name")
    travel_times = models.PositiveSmallIntegerField(verbose_name="Travel Time")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_from_city_set",
        verbose_name="Departing from a city",
    )
    to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_to_city_set",
        verbose_name="Arriving in a city",
    )
    planes = models.ManyToManyField(Plane, verbose_name="List of Planes")

    def __str__(self):
        return f"Route number {self.name} from {self.from_city} to {self.to_city}"

    class Meta:
        # verbose_name = "Route"
        # verbose_name_plural = "Routes"
        ordering = ["travel_times"]

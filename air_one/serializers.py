from rest_framework import serializers
from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = [
            "id",
            "name",
        ]


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plane
        fields = [
            "id",
            "name",
            "travel_time",
            "from_city",
            "to_city",
        ]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = [
            "id",
            "name",
            "travel_times",
            "from_city",
            "to_city",
            "planes",
        ]

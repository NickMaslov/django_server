from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "name"]

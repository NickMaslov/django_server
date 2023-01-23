from rest_framework import generics
from . import serializers, models


class CityList(generics.ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()

    # def get_queryset(self):
    #     return models.City.objects.filter(owner_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()

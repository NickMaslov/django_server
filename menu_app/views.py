from django.shortcuts import render
from rest_framework import generics
from . import serializers


class PlaceList(generics.ListAPIView):
    serializer_class = serializers.PlaceSerializer

    def get_queryset(self):
        return []

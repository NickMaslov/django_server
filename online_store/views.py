from django.shortcuts import render
from rest_framework import generics
from . import models, serializers


class ProductList(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get("keyword")
        if query == None:
            query = ""
        products = models.Product.objects.filter(name__icontains=query)
        # .order_by(
        #     "-createdAt"
        # )
        return products

    def perform_create(self, serializer):
        serializer.save()

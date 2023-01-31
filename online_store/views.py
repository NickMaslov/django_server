from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from . import models, serializers


class ProductList(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get("keyword")
        if query == None:
            query = ""
        products = models.Product.objects.filter(name__icontains=query).order_by(
            "-createdAt"
        )
        return products

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

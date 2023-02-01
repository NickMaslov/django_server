from rest_framework import generics, permissions
from django.contrib.auth.models import User
from ..serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # need a logic here where can sign up everyone


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
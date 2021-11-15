from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from users.serializers import CustomUserSerializer

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
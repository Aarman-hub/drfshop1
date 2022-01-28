from typing import Generic
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ArnaTokenObtainPairSerializer, RegisterSerializer
# Create your views here.

class ArnaTokenObtainPairView(TokenObtainPairView):
    serializer_class = ArnaTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

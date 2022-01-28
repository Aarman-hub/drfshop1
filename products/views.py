from django.shortcuts import render
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
# Create your views here.


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
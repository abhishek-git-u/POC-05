from eshop.models import Product
from django.shortcuts import render
from rest_framework import generics
from eshop.models import Product
from eshop.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
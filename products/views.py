from django.shortcuts import render
from rest_framework import generics
from .models import Category, Shape, Product
from .serializers import CategorySerializer, ShapeSerializer, ProductSerializer
# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ShapeListView(generics.ListAPIView):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
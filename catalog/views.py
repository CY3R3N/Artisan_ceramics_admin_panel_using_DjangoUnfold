from django.shortcuts import render
from rest_framework import generics
from .models import Catalog
from .serializers import CatalogSerializer
# Create your views here.
class CatalogListView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
class CatalogDetailView(generics.RetrieveAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
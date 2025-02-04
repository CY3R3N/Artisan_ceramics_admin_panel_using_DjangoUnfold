from django.shortcuts import render
from rest_framework import generics
from .models import HeroSection, BrandVideo, Showcase
from .serializers import HeroSectionSerializer, BrandVideoSerializer, ShowcaseSerializer
# Create your views here.
class HeroSectionSerializer(generics.ListAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
class BrandVideoListView(generics.ListAPIView):
    queryset = BrandVideo.objects.all()
    serializer_class = BrandVideoSerializer
class ShowcaseListView(generics.ListAPIView):
    queryset = Showcase.objects.all()
    serializer_class = ShowcaseSerializer
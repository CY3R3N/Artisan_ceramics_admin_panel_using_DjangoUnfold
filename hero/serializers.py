from rest_framework import serializers
from .models import HeroSection, Showcase , BrandVideo

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['title', 'video']
        
class BrandVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['title', 'video']

class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandVideo
        fields = ['product_image']
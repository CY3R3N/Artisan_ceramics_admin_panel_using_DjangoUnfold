from rest_framework import serializers
from .models import Catalog

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'cover_image','pdf_file']  # Adjust fields as per your requirements
        

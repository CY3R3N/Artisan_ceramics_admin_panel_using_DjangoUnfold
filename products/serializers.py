from rest_framework import serializers
from .models import Category, Shape, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']  # Adjust fields as per your requirements

class ShapeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested relationship

    class Meta:
        model = Shape
        fields = ['id', 'name', 'image', 'category']

class ProductSerializer(serializers.ModelSerializer):
    shape = ShapeSerializer()  # Nested relationship

    class Meta:
        model = Product
        fields = ['id', 'name', 'measurement', 'diameter', 'capacity', 'weight', 'image', 'created_at', 'updated_at', 'shape']

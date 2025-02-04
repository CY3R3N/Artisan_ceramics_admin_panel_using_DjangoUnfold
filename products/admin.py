from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Shape, Product

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)


@admin.register(Shape)
class ShapeAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'shape', 'measurement', 'diameter', 'capacity', 'weight', 'created_at', 'updated_at')
    list_filter = ('shape__category', 'shape')
    search_fields = ('name', 'shape__name', 'shape__category__name')
    readonly_fields = ('created_at', 'updated_at')

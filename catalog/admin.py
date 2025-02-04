from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Catalog
# Register your models here.

@admin.register(Catalog)
class CatalogAdmin(ModelAdmin):
    list_display = ('id', 'name', 'cover_image', 'pdf_file')
    search_fields = ('name',)
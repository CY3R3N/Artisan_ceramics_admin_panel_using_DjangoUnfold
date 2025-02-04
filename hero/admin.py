from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import HeroSection, Showcase, BrandVideo
# Register your models here.

@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    
@admin.register(BrandVideo)
class BrandVideoAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    
@admin.register(Showcase)
class ShowcaseAdmin(ModelAdmin):
    list_display = ('id', 'created_at')
    ordering = ('-created_at',)
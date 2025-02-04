from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import News
# Register your models here.
@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    list_filter = ('title', 'type', 'created_at')
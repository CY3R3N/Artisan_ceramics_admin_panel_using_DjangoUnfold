from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Directorboard

@admin.register(Directorboard)
class DirectorboardAdmin(ModelAdmin):
    list_display = ('name', 'designation','profile_picture')
    search_fields = ('name', 'designation')
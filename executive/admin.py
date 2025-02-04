from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Executive

@admin.register(Executive)
class ExecutiveAdmin(ModelAdmin):
    list_display = ('id', 'name', 'designation')
    search_fields = ('name', 'designation')
# Register your models here.

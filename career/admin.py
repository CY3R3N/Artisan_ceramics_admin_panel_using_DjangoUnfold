from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Job

@admin.register(Job)
class JobAdmin(ModelAdmin):
    list_display = ('position', 'job_type', 'location', 'salary', 'vacancy', 'deadline')
    list_filter = ('job_type', 'location', 'deadline')
    search_fields = ('position', 'location')

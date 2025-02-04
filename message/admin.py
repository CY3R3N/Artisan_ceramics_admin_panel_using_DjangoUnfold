from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Inbox
# Register your models here.

if admin.site.is_registered(Inbox):
    admin.site.unregister(Inbox)

class InboxAdmin(admin.ModelAdmin):
    # Hide the add button for the Inbox model in the admin panel
    def has_add_permission(self, request):
        return False

admin.site.register(Inbox, InboxAdmin)
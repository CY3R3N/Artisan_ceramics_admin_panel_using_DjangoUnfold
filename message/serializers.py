from rest_framework import serializers
from .models import Inbox

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ['name', 'email', 'message','department', 'is_read', 'created_at']
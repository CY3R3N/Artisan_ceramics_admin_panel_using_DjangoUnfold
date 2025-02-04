from rest_framework import serializers
from .models import Executive

class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = ['id', 'name', 'designation', 'profile_picture']
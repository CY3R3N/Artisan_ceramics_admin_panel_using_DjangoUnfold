from rest_framework import serializers
from .models import Directorboard

class DirectorboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directorboard
        fields = ['id', 'name', 'designation', 'profile_picture']
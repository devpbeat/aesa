# Create a serializer for the Project model.
from rest_framework import serializers
from .models import Project 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'status', 'project_code', 'plains')
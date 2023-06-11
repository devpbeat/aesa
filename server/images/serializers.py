# Create a serializer for the Images model.
from rest_framework import serializers
from .models import Images

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = [
            "image",
            "name",
            "desc"
        ]
        
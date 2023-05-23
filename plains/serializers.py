# Create a serializer for the Plain model.
from rest_framework import serializers
from .models import Plain 
from images.serializers import ImagesSerializer

class PlainSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Plain
        fields = [
            "name",
            "plain_code",
            "feeder",
            "zone",
            "delivery_number",
            "utm_coordinates",
            "observation",
            "images"
        ]

    def create(self, validated_data):
        images = validated_data.pop("images")
        plain = Plain.objects.create(**validated_data)
        for image in images:
            image = ImagesSerializer.create(ImagesSerializer(), validated_data=image)
            plain.images.add(image)
        return plain


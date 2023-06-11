# Create a serializer for the Customer model.
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "name",
            "ruc",
            "social_reason",
        ]
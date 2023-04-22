from rest_framework import serializers

from .models import Plain, Project


class ProjectSerializer(serializers.ModelSerializer):
    plains = serializers.PrimaryKeyRelatedField(
        queryset=Plain.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'ruc', 'social_reason', 'plains']


class PlainSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Plain
        fields = ['id', 'name', 'plain_code', 'customer', 'feeder', 'zone',
                  'delivery_number', 'utm_coordinates', 'observation', 'projects']

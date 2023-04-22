from rest_framework import viewsets

from .models import Plain, Project
from .serializers import PlainSerializer, ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'ruc', 'social_reason']


class PlainViewSet(viewsets.ModelViewSet):
    queryset = Plain.objects.all()
    serializer_class = PlainSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'plain_code', 'customer', 'feeder',
                        'zone', 'delivery_number', 'utm_coordinates', 'observation']

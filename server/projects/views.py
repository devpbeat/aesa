# Create a viewset for the Project model.
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from rest_framework_simplejwt import authentication
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [authentication.JWTAuthentication]


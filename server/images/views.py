# Create a viewset for the Images model.
from rest_framework.viewsets import ModelViewSet
from .models import Images
from .serializers import ImagesSerializer
from rest_framework_simplejwt import authentication

class ImagesViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    authentication_classes = [authentication.JWTAuthentication]


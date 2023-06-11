# Create a viewset for the Plain model.
from rest_framework.viewsets import ModelViewSet
from .models import Plain
from .serializers import PlainSerializer
from rest_framework_simplejwt import authentication

class PlainViewSet(ModelViewSet):
    queryset = Plain.objects.all()
    serializer_class = PlainSerializer
    authentication_classes = [authentication.JWTAuthentication]
    
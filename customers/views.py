# Create a viewset for the Customer model.
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import authentication
from .serializers import CustomerSerializer
from .models import Customer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [authentication.JWTAuthentication]
    
# Register the viewset with the URLconf.
from django.urls import path
from .views import CustomerViewSet

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customers'),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer'),
]

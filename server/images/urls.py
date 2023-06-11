# Register the viewset with the URLconf.
from django.urls import path
from .views import ImagesViewSet

urlpatterns = [
    path('images/', ImagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='images'),
    path('images/<int:pk>/', ImagesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='image'),
]
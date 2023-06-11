# Register the viewset with the URLconf.
from django.urls import path
from .views import ProjectViewSet

urlpatterns = [
    path('projects/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='projects'),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project'),
]

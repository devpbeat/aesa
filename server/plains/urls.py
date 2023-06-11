# Register the viewset with the URLconf.
from django.urls import path
from .views import PlainViewSet

urlpatterns = [
    path('plains/', PlainViewSet.as_view({'get': 'list', 'post': 'create'}), name='plains'),
    path('plains/<int:pk>/', PlainViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='plain'),
]
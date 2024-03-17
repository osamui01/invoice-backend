from rest_framework import routers
from services.views import ServiceViewSet


service_router = routers.DefaultRouter()
service_router.register(r'services', ServiceViewSet, basename='services')

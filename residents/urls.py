from rest_framework import routers
from residents.views import ResidentViewSet


resident_router = routers.DefaultRouter()
resident_router.register(r'residents', ResidentViewSet, basename='residents')

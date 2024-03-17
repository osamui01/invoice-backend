from rest_framework import routers
from carehomes.views import CareHomeViewSet


carehome_router = routers.DefaultRouter()
carehome_router.register(r'carehomes', CareHomeViewSet, basename='carehomes')

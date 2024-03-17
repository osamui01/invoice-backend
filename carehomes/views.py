from rest_framework import viewsets
from carehomes.models import CareHome
from carehomes.serializers import CareHomeSerializer


class CareHomeViewSet(viewsets.ModelViewSet):
    queryset = CareHome.objects.all()
    serializer_class = CareHomeSerializer

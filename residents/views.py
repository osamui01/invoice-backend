from rest_framework import viewsets
from residents.models import Resident
from residents.serializers import ResidentSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

from rest_framework import serializers
from carehomes.models import *


class CareHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareHome
        fields = '__all__'

from rest_framework import viewsets
from company_settings.models import CompanySetting
from company_settings.serializers import CompanySettingSerializer


class CompanySettingViewSet(viewsets.ModelViewSet):
    queryset = CompanySetting.objects.all()
    serializer_class = CompanySettingSerializer

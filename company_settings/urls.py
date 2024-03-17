from rest_framework import routers
from company_settings.views import CompanySettingViewSet


company_setting_router = routers.DefaultRouter()
company_setting_router.register(r'company-settings', CompanySettingViewSet, basename='company-settings')

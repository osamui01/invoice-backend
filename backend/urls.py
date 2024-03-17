from django.contrib import admin
from django.urls import path, include

from residents.urls import resident_router as resident_router
from carehomes.urls import carehome_router as carehome_router
from services.urls import service_router as service_router
from company_settings.urls import company_setting_router as company_setting_router
from invoices.urls import invoice_router as invoice_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api-1/', include(resident_router.urls)),
    path('api-2/', include(carehome_router.urls)),
    path('api-3/', include(service_router.urls)),
    path('api-4/', include(company_setting_router.urls)),
    path('api-5/', include(invoice_router.urls)),
]

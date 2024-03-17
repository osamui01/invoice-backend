from rest_framework import routers
from invoices.views import InvoiceViewSet


invoice_router = routers.DefaultRouter()
invoice_router.register(r'invoices', InvoiceViewSet, basename='invoices')
invoice_router.register(r'invoice-items', InvoiceViewSet, basename='invoice-items')

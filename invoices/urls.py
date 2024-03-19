from rest_framework import routers
from invoices.views import InvoiceViewSet, InvoiceItemViewSet


invoice_router = routers.DefaultRouter()
invoice_router.register(r'invoices', InvoiceViewSet, basename='invoices')
invoice_router.register(r'invoice-items', InvoiceItemViewSet, basename='invoice-items')

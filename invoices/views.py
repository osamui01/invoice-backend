from rest_framework import viewsets
from invoices.models import Invoice, InvoiceItem
from invoices.serializers import InvoiceSerializer, InvoiceItemSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

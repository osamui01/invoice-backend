import uuid
from django.db import models
from django.utils import timezone

from carehomes.models import CareHome
from company_settings.models import CompanySetting
from residents.models import Resident
from services.models import Service


class Invoice(models.Model):
    # UUID Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    # Reference Fields
    carehome = models.ForeignKey(CareHome, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name="invoice_care_home")

    # Invoice Fields
    number = models.CharField(max_length=40, blank=True, null=True, verbose_name="Invoice Number")
    status = models.CharField(max_length=20, blank=True, null=True, verbose_name="Status")
    item = models.ManyToManyField('InvoiceItem', blank=True, related_name="invoice_items")
    company_settings = models.ForeignKey(CompanySetting, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="invoice_company_setting")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        self.last_updated = timezone.localtime(timezone.now())

        if not self.number:
            self.number = f"{self.date_created.strftime('%y%m%d')}-{self.carehome.name}" if self.carehome else ""

        super(Invoice, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Invoices"

    def __str__(self):
        return '{} {}'.format(self.number, self.status)


class InvoiceItem(models.Model):
    # UUID Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    # Invoice Item Fields
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name="invoice_item_invoice")
    resident = models.ForeignKey(Resident, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name="invoice_item_resident")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name="invoice_item_service")

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        super(InvoiceItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Invoice Items"

    def __str__(self):
        return '{} {}'.format(self.invoice, self.resident)

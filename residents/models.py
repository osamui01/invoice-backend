import uuid
from django.db import models
from django.utils import timezone

from carehomes.models import CareHome


class Resident(models.Model):
    # UUID Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Resident Fields
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name="Title")
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name="Name")
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, blank=True, null=True, verbose_name="Gender")
    address = models.TextField(max_length=200, blank=True, null=True, verbose_name="Address")
    postcode = models.CharField(max_length=10, blank=True, null=True, verbose_name="Postcode")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Contact Number")
    email = models.CharField(max_length=60, blank=True, null=True, verbose_name="Email Address")

    # Reference Fields
    carehome = models.ForeignKey(CareHome, blank=True, on_delete=models.SET_NULL, null=True)

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        self.last_updated = timezone.localtime(timezone.now())

        super(Resident, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Resident"

    def __str__(self):
        return '{}'.format(self.name)

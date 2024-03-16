from django.db import models
from django.utils import timezone


class CompanySetting(models.Model):
    # Company Setting Fields
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name="Company Name")
    number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    sort_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Sort Code")
    acc_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Account Number")

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        self.last_updated = timezone.localtime(timezone.now())

        super(CompanySetting, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Company Settings"

    def __str__(self):
        return '{} {}'.format(self.name, self.number)


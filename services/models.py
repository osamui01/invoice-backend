from django.db import models
from django.utils import timezone


class Service(models.Model):
    # Service Fields
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name="Service")
    price = models.IntegerField(blank=True, null=True, verbose_name="Price")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        self.last_updated = timezone.localtime(timezone.now())

        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return '{} £{}'.format(self.name, self.price)

from django.db import models
import uuid
from django.utils import timezone


class CareHome(models.Model):
    # UUID Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Care Home Fields
    name = models.CharField(max_length=100)

    # Utility Fields
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # Dynamic Save
    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.now()

        self.last_updated = timezone.localtime(timezone.now())

        super(CareHome, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Care Home"

    def __str__(self):
        return '{}'.format(self.name)


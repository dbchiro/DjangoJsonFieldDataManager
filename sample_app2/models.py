# Create your models here.
from django.db import models

from jsondata_manager.models import ExtraDataMixin

# Create your models here.


class SampleApp2A(ExtraDataMixin):
    label = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.validate_extra_data()  # Validate before saving
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return self.label


class SampleApp2B(ExtraDataMixin):
    label = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.validate_extra_data()  # Validate before saving
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return self.label

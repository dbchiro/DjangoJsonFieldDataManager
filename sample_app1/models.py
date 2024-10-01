from django.db import models

from jsondata_manager.models import ExtraDataMixin

# Create your models here.


class SampleApp1(ExtraDataMixin):
    label = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.validate_extra_data()  # Validate before saving
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return self.label

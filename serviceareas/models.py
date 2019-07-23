from providers.models import BaseModel, Provider
from django.db import models
from django.contrib.postgres import fields
from django.contrib.gis.db import models as geo_models


class ServiceArea(BaseModel):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    coordinates = fields.ArrayField(
        fields.ArrayField(
            models.DecimalField(max_digits=9, decimal_places=6)
        )
    )

    class Meta:
        ordering = ['-created']

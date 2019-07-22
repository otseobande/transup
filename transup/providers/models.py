import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UuidModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Provider(UuidModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField()
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=20)


import uuid
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Provider(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField()
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=20)



from django.db import models
from core.models import BaseModel


class Certification(BaseModel):

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50, unique=True)

    description = models.TextField()

    def __str__(self):
        return self.name
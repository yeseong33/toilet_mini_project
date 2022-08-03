from pyexpat import model
from django.db import models

from core.models import CoreModel

class User(CoreModel):

    GENDER = [
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN')
    ]
    latitude = models.DecimalField(help_text="위도", max_digits=500, decimal_places=2)
    longitude = models.DecimalField(help_text="경도", max_digits=500, decimal_places=2)
    gender = models.CharField(max_length=5, choices=GENDER)
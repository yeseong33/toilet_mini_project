from enum import Enum
from django.db import models

from toilet_app.core.models import CoreModel

class Toilet(CoreModel):

    GENDER = [
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN')
    ]
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    gender = models.CharField(max_length=5, choices=GENDER)
    isBisexual = models.BooleanField(default=False)
    toiletNum = models.IntegerField(default=0, null=True, help_text="대변기의 숫자")
    urinalNum = models.IntegerField(default=0, null=True, help_text="소변기의 숫자")
    disabledToiletNum = models.IntegerField(default=0, null=True, help_text="장애인용 대변기 숫자")
    disabledUrinalNum = models.IntegerField(default=0, null=True, help_text="장애인용 소변기 숫자")
    childToiletNum = models.IntegerField(default=0, null=True, help_text="어린이용 대변기 숫자")
    childUrinalNum = models.IntegerField(default=0, null=True, help_text="어린이용 소변기 숫자")
    managementAgency = models.CharField(max_length=140, help_text="설치 기관명")
    phoneNumber = models.CharField(max_length=11)
    openTime = models.CharField(max_length=140)
    installationDate = models.CharField(max_length=140, null=False)
    latitude = models.DecimalField(help_text="위도")
    longitude = models.DecimalField(help_text="경도")

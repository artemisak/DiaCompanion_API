from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class DiaUsers(AbstractUser):
    middle_name = models.CharField(blank=True, max_length=150)
    birth_date = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    attending_doctor = models.CharField(max_length=150, default="Попова Полина Викторовна")
    app_type = models.CharField(max_length=150, default="Dia I")

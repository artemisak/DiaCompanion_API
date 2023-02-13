from django.db import models


# Create your models here.
class DiaUsers(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    email = models.CharField(unique=True, max_length=80)
    password = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    birth_date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    attending_doctor = models.CharField(max_length=80)
    app_type = models.CharField(max_length=80)

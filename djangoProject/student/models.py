from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=16, null=True)
    phone = models.CharField(max_length=64, null=True)
    age = models.IntegerField(default=0, null=True)

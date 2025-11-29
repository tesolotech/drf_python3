from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=13)

from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    birth_day = models.DateField()

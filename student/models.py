from django.db import models

# Create your models here.

class StudentModel(models.Model):

    name = models.CharField(max_length=20)

    roll_no = models.IntegerField()

    department = models.CharField(max_length=30)

    email = models.EmailField()

    marks = models.IntegerField()


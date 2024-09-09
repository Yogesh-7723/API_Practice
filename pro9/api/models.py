from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    edu = models.IntegerField()
    result = models.CharField(choices=(('Pass','PASS'),('Fail','FAIL')),max_length=5)

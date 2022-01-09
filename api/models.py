from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=90)
    company_name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=250)
    web = models.CharField(max_length=100)
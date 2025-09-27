from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length = 30)
    age  = models.IntegerField()
    designation = models.CharField(max_length = 30)
    

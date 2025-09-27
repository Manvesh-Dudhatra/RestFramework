from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    branch = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

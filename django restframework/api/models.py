from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length = 30)
    age  = models.IntegerField()
    designation = models.CharField(max_length = 30)
    owner = models.ForeignKey(User, related_name = "employee", on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = "comments")
    comment = models.TextField()
    
class Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    branch = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length = 20)
    author = models.ForeignKey(Author, related_name  = "books", on_delete = models.CASCADE)
    
    

    

    


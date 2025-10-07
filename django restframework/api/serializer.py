from rest_framework import serializers
from .models import Student, Employee, Comment, Blog, Author, Book
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(many = True, queryset=Employee.objects.all())
    
    class Meta:
        model = User
        fields = ["id", "username", 'employee']
        
class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Employee
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
               
class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = "__all__"
        
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"
        
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many = True, read_only = True ,view_name = "book-detail")
    class Meta:
        model = Author
        fields ="__all__"
        
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

        

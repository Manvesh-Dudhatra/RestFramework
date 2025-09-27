 
from students.models import Student
from rest_framework.response import Response
from .serializer import StudentSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404


@api_view(['GET', 'POST'])
def StudentView(request):
    if request.method =="GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = 200)

    elif request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        
        else:
            return Response(serializer.errors)

@api_view(['GET', "PUT", "DELETE"])        
def StudentDetails(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except:
        if Student.DoesNotExist():
            return Response(status = 404)
        
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status = 200)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        else:
            return Response(serializer.errors)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status = 204)
    
    
class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status = 200)
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        
        else:
            return Response(serializer.errors)
        
class EmployeeDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk = pk)
        except Student.DoesNotExist():
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status = 200)
        
    def put(self, request, pk):
        student  = self.get_object(pk)
        serializer = EmployeeSerializer(student , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        else:
            return Response(serializer.errors)
            
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status = 204)
            
                
        
   
    

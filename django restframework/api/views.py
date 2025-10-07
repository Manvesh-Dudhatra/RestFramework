from django.shortcuts import render, get_object_or_404
from .models import Student, Employee, Blog, Comment, Book, Author
from rest_framework.response import Response
from .serializer import StudentSerializer, EmployeeSerializer, BlogSerializer, CommentSerializer, UserSerializer, AuthorSerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets, permissions, reverse, renderers
# from .paginations import CustomePagination
from .filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(["GET"])
def api_root(request, format = None):
    return Response({
        "employee":reverse("employee-list", request = request, format = format),
        "users":reverse("user-list", request = request, format = format)
    })


   
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
    
    
'''class EmployeeView(APIView):
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


# mixins
class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self , request):
        return self.create(request)

# mixins
class EmployeeDetailsView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
generics
class EmployeeView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailsView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"



viewsets
class EmployeeView(viewsets.ViewSet):
    def list(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status = 200)
    
    def create(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk):
        employee = get_object_or_404(Employee, pk = pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        
    
    def update(self, request, pk):
        employee = get_object_or_404(Employee, pk = pk)
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk = pk)
        employee.delete()
        return Response(status = 204)'''

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'url'
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'designation']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # filterset_class = EmployeeFilter
    # pagination_class = CustomePagination


#using foreign key   
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["id"]

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    


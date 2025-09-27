from django.urls import path
from . import views

urlpatterns = [
    path('students/' , views.StudentView),
    path('students/<int:pk>/', views.StudentDetails),
    
    path('employee/', views.EmployeeView.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetailsView.as_view())
]
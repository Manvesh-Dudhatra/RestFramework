import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name = "designation", lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name = "name", lookup_expr='icontain')
    id = django_filters.RangeFilter(field_name = 'id')
    
    class Meta:
        models = Employee
        fields = ['designation', 'emp_name', 'id']
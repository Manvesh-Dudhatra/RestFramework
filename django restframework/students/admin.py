from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "branch",)

admin.site.register(Student, StudentAdmin)

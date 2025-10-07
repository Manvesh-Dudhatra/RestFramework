from django.contrib import admin
from .models import Blog, Comment, Employee, Student, Author, Book

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog", "comment",)
admin.site.register(Comment, CommentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "designation")
admin.site.register(Employee, EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "branch",)
admin.site.register(Student, StudentAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", 'author',)
admin.site.register(Book, BookAdmin)

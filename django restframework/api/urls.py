from django.urls import path, include
from . import views
from .views import api_root, EmployeeView, UserView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r"employee", views.EmployeeView, basename = "employee"),
router.register(r"users", views.UserView, basename = "user"),
router.register(r"authors", views.AuthorView, basename = "author"),
router.register(r"books", views.BookView, basename = "book")

# employee_list = EmployeeView.as_view({
#     'get':'list',
#     'post':'create',
# })

# user_list = UserView.as_view({
#     'get':'list',
#     'post':'create',
# })

urlpatterns = [
    # path("", views.api_root),
    path('students/' , views.StudentView),
    path('students/<int:pk>/', views.StudentDetails),
    # path('employee/<int:pk>/', views.Employee, name = 'employee-details'),
    
    
    # path('employee/', views.EmployeeView.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetailsView.as_view()),
    path('', include(router.urls)),
    
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),
    
    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()), 
    # path('employee', employee_list, name = "employee-list"),
    # path('users', user_list, name = "user-list"),
      
]

# urlpatterns = format_suffix_patterns(urlpatterns)
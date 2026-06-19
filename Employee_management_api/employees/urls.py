from django.urls import path
from .views import (
    DepartmentListCreateView, DepartmentDetailView,
    DesignationListCreateView, DesignationDetailView,
    EmployeeListCreateView, EmployeeDetailView
)

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', DepartmentDetailView.as_view()),
    
    path('designations/', DesignationListCreateView.as_view()),
    path('designations/<int:pk>/', DesignationDetailView.as_view()),
    
    path('employees/', EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeDetailView.as_view()),
]

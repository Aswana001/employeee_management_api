from rest_framework import generics, mixins, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Department, Designation, Employee
from .serializers import (
DepartmentSerializer,
DesignationSerializer,
EmployeeSerializer
)
from .pagination import StandardResultsSetPagination



class DepartmentListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DepartmentDetailView(
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,
generics.GenericAPIView
):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = [IsAdminUser]


    def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
     return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class DesignationListCreateView(
mixins.ListModelMixin,
mixins.CreateModelMixin,
generics.GenericAPIView
):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
         return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)


class DesignationDetailView(
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,
generics.GenericAPIView
):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    #permission_classes = [IsAdminUser]


    def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
     return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EmployeeListCreateView(
mixins.ListModelMixin,
mixins.CreateModelMixin,
generics.GenericAPIView
):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

  #permission_classes = [IsAuthenticated]

pagination_class = StandardResultsSetPagination

filter_backends = [
    DjangoFilterBackend,
    filters.SearchFilter
]

filterset_fields = [
    'department',
    'designation',
    'is_active'
]

search_fields = [
    'employee_id',
    'first_name',
    'last_name',
    'email'
]

def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class EmployeeDetailView(
   mixins.RetrieveModelMixin,
   mixins.UpdateModelMixin,
   mixins.DestroyModelMixin,
   generics.GenericAPIView
):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

#permission_classes = [IsAdminUser]

def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

def patch(self, request, *args, **kwargs):
    return self.partial_update(request, *args, **kwargs)

def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

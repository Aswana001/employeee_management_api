from rest_framework import serializers
from .models import Department, Designation, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    # READ (GET)
    department = DepartmentSerializer(read_only=True)
    designation = DesignationSerializer(read_only=True)

    # WRITE (POST/PUT/PATCH)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="department",
        write_only=True
    )

    designation_id = serializers.PrimaryKeyRelatedField(
        queryset=Designation.objects.all(),
        source="designation",
        write_only=True
    )

    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "department",
            "designation",
            "department_id",
            "designation_id",
            "date_joined",
            "is_active",
        ]
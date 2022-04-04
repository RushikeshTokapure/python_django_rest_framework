from rest_framework import serializers
from django.contrib.auth.models import User

from Quickstart.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # to display all fields
        # OR
        # fields = ['name', 'email']  # to display specific fields  


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

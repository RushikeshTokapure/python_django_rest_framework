from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, BasePermission

from RelationshipsAndHyperlinkedAPIs.models import Instructor, Course
from RelationshipsAndHyperlinkedAPIs.serializer import InstructorSerializer, CourseSerializer

# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        else:
            return False


# JSON Web Token Authentication

class InstructorListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


# TokenAuthentication

# class InstructorListView(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
#     serializer_class = InstructorSerializer
#     queryset = Instructor.objects.all()


# Relationships


# class InstructorListView(generics.ListCreateAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
#     serializer_class = InstructorSerializer
#     queryset = Instructor.objects.all()
#
#
# class CourseListView(generics.ListCreateAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()


# HyperlinkedAPIs


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

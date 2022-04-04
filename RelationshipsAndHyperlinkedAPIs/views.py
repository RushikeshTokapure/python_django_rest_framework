from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from RelationshipsAndHyperlinkedAPIs.models import Instructor, Course
from RelationshipsAndHyperlinkedAPIs.serializer import InstructorSerializer, CourseSerializer

# Relationships


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# HyperlinkedAPIs


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

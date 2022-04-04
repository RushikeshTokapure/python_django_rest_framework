from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from ViewsetsAndRouters.models import Course
from ViewsetsAndRouters.serializer import CourseSerializer


# Create your views here.


# Model ViewSet

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# ViewSet

# class CourseViewSet(ViewSet):
#     def list(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def retrieve(self, request, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     def update(self, request, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def destroy(self, request, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

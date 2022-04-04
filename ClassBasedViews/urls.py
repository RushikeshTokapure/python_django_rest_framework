from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('api/courses', views.CourseListView.as_view(), name="Course_List_View"),
    path('api/courses/<int:pk>', views.CourseDetailView.as_view(), name="Course_Detail_View"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

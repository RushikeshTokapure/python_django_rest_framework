from django.urls import path
from . import views

urlpatterns = [
    path('api/courses', views.course_list_view, name="course_list_view"),
    path('api/courses/<int:pk>', views.course_detail_view, name="course_detail_view")
]

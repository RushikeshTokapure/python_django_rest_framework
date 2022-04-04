from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from RelationshipsAndHyperlinkedAPIs import views

urlpatterns = [
    path('api/instructors', views.InstructorListView.as_view()),
    path('api/courses', views.CourseListView.as_view()),
    path('api/courses/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('api/instructors/<int:pk>', views.InstructorDetailView.as_view(), name='instructor-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

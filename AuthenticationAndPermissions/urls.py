from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from RelationshipsAndHyperlinkedAPIs import views

urlpatterns = [
    path('api/instructors', views.InstructorListView.as_view()),
    path('api/courses', views.CourseListView.as_view()),
    path('api/courses/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('api/instructors/<int:pk>', views.InstructorDetailView.as_view(), name='instructor-detail'),
    path('api/auth/login/', obtain_auth_token, name='create-token'),

    path('api/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh")
]

urlpatterns = format_suffix_patterns(urlpatterns)

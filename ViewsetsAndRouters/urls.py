from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ViewsetsAndRouters import views

# create router and register our view-sets with it

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='course')

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('api/', include(router.urls)),
]

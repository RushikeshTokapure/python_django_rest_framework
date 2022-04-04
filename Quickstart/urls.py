from . import views
from django.urls import path


urlpatterns = [
    path('api/employees', views.employee_list_view, name="employee_list_view"),
    path('api/employees/<int:pk>', views.employee_detail_view, name="employee_detail_view"),
    path('api/users', views.user_list_view, name="user_list_view"),
]

from django.contrib import admin

# Register your models here.
from AuthenticationAndPermissions.models import Instructor, Course

admin.site.register(Instructor)
admin.site.register(Course)

from django.contrib import admin

from .models import *

# Register your models here.

mymodels=[users_domain,course_students,course_tests,student_ppa_profiles,courses,course_modules]
admin.site.register(mymodels)


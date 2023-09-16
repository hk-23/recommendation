from django.contrib import admin
from .models import *

# Register your models here.

mymodels=[language_wise,module_wise,subtopic_wise]
admin.site.register(mymodels)
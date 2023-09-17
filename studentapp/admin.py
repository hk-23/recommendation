from django.contrib import admin
from .models import *

# Register your models here.

mymodels=[language_wise,module_wise,subtopic_wise,company_recommendation]
admin.site.register(mymodels)
from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard/',landing_page,name='landing_page'),
	path('temp/',show_temp,name='temp_page'),
]
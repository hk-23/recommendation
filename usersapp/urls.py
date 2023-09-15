from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('login/',user_login,name='login'),
	path('logout/',logout_view,name='logout'),
	path('profile/',profile_view,name='profile'),
]
from django.shortcuts import render
from usersapp.decorators import *
from .models import *
from usersapp.models import *

# Create your views here.

# @is_student
def landing_page(request):
	user_obj = User.objects.get(id=request.user.id)
	lang_data = language_wise.objects.filter(email=user_obj)
	context = {'lang_data': lang_data}
	return render(request,'studentapp/dashboard.html',context=context)


# def landing_page(request):
# 	context = {
# 		'help': 'pls'
# 	}
# 	return render(request,'studentapp/dashboard.html',context=context)
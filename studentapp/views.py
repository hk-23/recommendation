from django.shortcuts import render
from usersapp.decorators import *
from .models import *
from usersapp.models import *

# Create your views here.

# @is_student
def landing_page(request):
	user_obj = User.objects.get(id=request.user.id)
	lang_data = language_wise.objects.filter(email=user_obj)

	max_entry = max(lang_data, key=lambda x: x.attended())
	
	max_questions_attended = max_entry.attended
	max_lang_used = max_entry.language_used
	
	context = {
		'lang_data': lang_data,
		'max_lang_used': max_lang_used
	}
	return render(request,'studentapp/dashboard.html',context=context)


# def landing_page(request):
# 	context = {
# 		'help': 'pls'
# 	}
# 	return render(request,'studentapp/dashboard.html',context=context)
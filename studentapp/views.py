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
	max_accuracy = max_entry.accuracy
	max_questions_solved = max_entry.Questions_Correct


	topic_data = module_wise.objects.filter(email=user_obj).order_by('-Questions_Correct')[:5]


	skilled_topic = max(topic_data, key=lambda x: x.attended())

	st_attended = skilled_topic.attended
	st_topic = skilled_topic.ModuleName
	st_accuracy =skilled_topic.accuracy
	st_solved = skilled_topic.Questions_Correct

	
	context = {
		'lang_data': lang_data,
		'topic_data': topic_data,
		'max_lang_used': max_lang_used,
		'accuracy': max_accuracy,
		'attended':max_questions_attended,
		'solved': max_questions_solved,
		'skilled_topic': {
			'attended': st_attended,
			'topic': st_topic,
			'accuracy': st_accuracy,
			'solved': st_solved
		}
	}
	return render(request,'studentapp/dashboard.html',context=context)


def show_temp(request):
	return render(request,'temp.html')


def my_courses(request):
	return render(request,'studentapp/mycourses.html')


# def landing_page(request):
# 	context = {
# 		'help': 'pls'
# 	}
# 	return render(request,'studentapp/dashboard.html',context=context)
from django.shortcuts import render
from usersapp.decorators import *
from .models import *
from usersapp.models import *
from users.models import *

# Create your views here.

# @is_student
def landing_page(request):
	user_obj = User.objects.get(id=request.user.id)
	lang_data = language_wise.objects.filter(email=user_obj)

	max_entry = max(lang_data, key=lambda x: x.Questions_Correct)
	
	max_questions_attended = max_entry.attended
	max_lang_used = max_entry.language_used
	max_accuracy = max_entry.accuracy
	max_questions_solved = max_entry.Questions_Correct


	topic_data = module_wise.objects.filter(email=user_obj).order_by('-Questions_Correct')[:5]


	skilled_topic = max(topic_data, key=lambda x: x.Questions_Correct)

	st_attended = skilled_topic.attended
	st_topic = skilled_topic.ModuleName
	st_accuracy =skilled_topic.accuracy
	st_solved = skilled_topic.Questions_Correct


	# Company Based Course Recommendation:

	cr = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("-accuracy")
	cr_top = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("-accuracy")[:3]
	cr_bot = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("accuracy")[:3]

	total_comp = len(cr)

	if total_comp > 5:
		final_cr = cr_top | cr_bot
	elif total_comp > 3:
		final_cr = cr_top | company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("accuracy")[:(total_comp-3)]
	else:
		final_cr = cr_top

	for com in final_cr:
		com.recm_courses = company_mapping.objects.filter(company=com.company)[:3]

		com.topic_to_look = company_subtopic.objects.filter(company=com.company)[:5]


	
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
		},
		'final_cr': final_cr
	}
	return render(request,'studentapp/dashboard.html',context=context)


def show_temp(request):

	user_obj = User.objects.get(id=request.user.id)

	email = user_obj.email

	user_domain_obj = users_domain.objects.filter(email=email)[:1]

	user_domain_obj = users_domain.objects.get(pk=user_domain_obj)

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

	cr = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("-accuracy")
	cr_top = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("-accuracy")[:3]
	cr_bot = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("accuracy")[:3]

	total_comp = len(cr)

	if total_comp > 5:
		final_cr = cr_top | cr_bot
	elif total_comp > 3:
		final_cr = cr_top | company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("accuracy")[:(total_comp-3)]
	else:
		final_cr = cr_top

	for com in final_cr:
		com.recm_courses = company_mapping.objects.filter(company=com.company)[:3]

		com.topic_to_look = company_subtopic.objects.filter(company=com.company)[:5]
	
	context = {
		'cr_top': cr_top,
		'final_cr': final_cr,
		'max_lang_used': max_lang_used,
		'user_domain_obj': user_domain_obj
	}
	return render(request,'temp.html',context=context)


def my_courses(request):
	courses_enrolled = course_students.objects.filter(email=request.user.id)	
	# cr = company_recommendation.objects.filter(email=user_obj,attended__gt=20,total_topics__gt=1).order_by("-accuracy")

	context = {
		'courses_enrolled': courses_enrolled
	}
	return render(request,'studentapp/mycourses.html', context=context)


# def landing_page(request):
# 	context = {
# 		'help': 'pls'
# 	}
# 	return render(request,'studentapp/dashboard.html',context=context)
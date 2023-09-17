import uuid
from django.db import models
from users.models import company

# Create your models here.
	
class language_wise(models.Model):
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	email = models.ForeignKey("usersapp.user",on_delete=models.CASCADE,default=None,null=True)
	language_used = models.CharField(max_length=50)
	student_marks = models.FloatField()
	total_marks = models.FloatField()
	MarksPercentage = models.FloatField(null=True)
	Hard_correct_questions = models.IntegerField(default=0)
	Easy_correct_questions = models.IntegerField(default=0)
	medium_correct_questions = models.IntegerField(default=0)
	Questions_Correct = models.IntegerField(default=0)
	Questions_wrong = models.IntegerField(default=0)
	Questions_skipped = models.IntegerField(default=0)
	Questions_partial_correct = models.IntegerField(default=0)
	Questions_not_viewed = models.IntegerField(default=0)
	testcase_passed = models.IntegerField(default=0)
	no_of_testcases = models.IntegerField(default=0)
	testcase_percentage = models.FloatField()


	def attended(self):
		return self.Questions_Correct + self.Questions_wrong + self.Questions_skipped + self.Questions_partial_correct + self.Questions_not_viewed

	def accuracy(self):
		return (self.Questions_Correct / int(self.attended())) * 100
	

class module_wise(models.Model):
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	email = models.ForeignKey("usersapp.user",on_delete=models.CASCADE,default=None,null=True)
	ModuleName = models.CharField(max_length=50)
	student_marks = models.FloatField()
	total_marks = models.FloatField()
	MarksPercentage = models.FloatField(null=True)
	Hard_correct_questions = models.IntegerField(default=0)
	Easy_correct_questions = models.IntegerField(default=0)
	medium_correct_questions = models.IntegerField(default=0)
	Questions_Correct = models.IntegerField(default=0)
	Questions_wrong = models.IntegerField(default=0)
	Questions_skipped = models.IntegerField(default=0)
	Questions_partial_correct = models.IntegerField(default=0)
	Questions_not_viewed = models.IntegerField(default=0)
	testcase_passed = models.IntegerField(default=0)
	no_of_testcases = models.IntegerField(default=0)
	testcase_percentage = models.FloatField()	

	def attended(self):
		return self.Questions_Correct + self.Questions_wrong + self.Questions_skipped + self.Questions_partial_correct + self.Questions_not_viewed

	def accuracy(self):
		return (self.Questions_Correct / int(self.attended())) * 100
	

class subtopic_wise(models.Model):
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	email = models.ForeignKey("usersapp.user",on_delete=models.CASCADE,default=None,null=True)
	subtopic_name = models.CharField(max_length=50)
	student_marks = models.FloatField()
	total_marks = models.FloatField()
	MarksPercentage = models.FloatField(null=True)
	Hard_correct_questions = models.IntegerField(default=0)
	Easy_correct_questions = models.IntegerField(default=0)
	medium_correct_questions = models.IntegerField(default=0)
	Questions_Correct = models.IntegerField(default=0)
	Questions_wrong = models.IntegerField(default=0)
	Questions_skipped = models.IntegerField(default=0)
	Questions_partial_correct = models.IntegerField(default=0)
	Questions_not_viewed = models.IntegerField(default=0)
	testcase_passed = models.IntegerField(default=0)
	no_of_testcases = models.IntegerField(default=0)
	testcase_percentage = models.FloatField()	

	def attended(self):
		return self.Questions_Correct + self.Questions_wrong + self.Questions_skipped + self.Questions_partial_correct + self.Questions_not_viewed

	def accuracy(self):
		return (self.Questions_Correct / int(self.attended())) * 100


class company_recommendation(models.Model):
	email = models.ForeignKey("usersapp.user",on_delete=models.CASCADE,default=None,null=True)
	company = models.ForeignKey("users.company",on_delete=models.CASCADE,default=None,null=True)
	comp = models.CharField(max_length=100,default=None)
	total_topics = models.IntegerField(default=0)
	Questions_Correct = models.IntegerField(default=0)
	attended = models.IntegerField(default=0)
	accuracy = models.FloatField()

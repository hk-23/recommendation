import uuid
from django.db import models

# Create your models here.

class users_domain(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

	users_domain_id = models.BigIntegerField(primary_key=True)
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	school_id = models.UUIDField(default=uuid.uuid4,editable=True)
	school_name = models.CharField(max_length=50)
	school_code = models.CharField(max_length=50,)
	email = models.EmailField()
	name = models.CharField(max_length=50,null=True)
	phone = models.JSONField(default=dict,null=True)
	gender = models.CharField(max_length=50,null=True)
	profile_pic = models.CharField(max_length=250,null=True)
	roll_no = models.CharField(max_length=50,null=True)
	badge = models.BigIntegerField(default=0)
	superbadge = models.BigIntegerField(default=0)
	dob = models.DateField(null=True)
	branch_id = models.UUIDField(default=uuid.uuid4,editable=True)
	branch_name = models.CharField(max_length=50,blank=True)
	batch_id = models.UUIDField(default=uuid.uuid4,null=True,editable=True)
	batch = models.CharField(max_length=50,null=True)
	department_id = models.UUIDField(default=uuid.uuid4,null=True,editable=True)
	department_name	= models.CharField(max_length=50,null=True)
	degree_id = models.UUIDField(default=uuid.uuid4,null=True,editable=True)
	degree = models.CharField(max_length=50,null=True)



class course_students(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

	id = models.BigIntegerField(primary_key=True)
	c_id = models.UUIDField(default=uuid.uuid4,editable=True)
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	badge = models.BigIntegerField(default=0)
	superbadge = models.BigIntegerField(default=0)
	penalty_points= models.BigIntegerField(default=0)
	course_completion= models.FloatField(default=0)
	last_viewed = models.DateField(null=True)
	branch_id = models.UUIDField(default=uuid.uuid4,editable=True)
	department_id = models.UUIDField(default=uuid.uuid4,null=True,editable=True)


class course_tests(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

	id = models.BigIntegerField(primary_key=True)
	c_id = models.UUIDField(default=uuid.uuid4,editable=True)
	school_id = models.UUIDField(default=uuid.uuid4,editable=True)
	c_type = models.CharField(max_length=50,null=True)
	branch_id = models.UUIDField(default=uuid.uuid4,editable=True)
	t_type = models.CharField(max_length=50,blank=True)
	t_name	= models.CharField(max_length=50,null=True)
	c_name	= models.CharField(max_length=50,null=True)
	t_id = models.UUIDField(default=uuid.uuid4,null=True,editable=True)
	Module_name = models.CharField(max_length=50,null=True)


class student_ppa_profiles(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

	s_profile_id = models.BigIntegerField(primary_key=True)
	user_id = models.UUIDField(default=uuid.uuid4,editable=True)
	school_id = models.UUIDField(default=uuid.uuid4,editable=True)
	tenth_marks = models.FloatField(null=True)
	is_tenth_percentage = models.IntegerField(null=True)
	twelfth_marks = models.FloatField(null=True)
	is_twelfth_percentage = models.IntegerField(null=True)
	diploma_marks = models.FloatField(null=True)
	is_diploma_percentage = models.IntegerField(null=True)
	ug_marks = models.FloatField(null=True)
	is_ug_percentage = models.IntegerField(null=True)
	pg_marks = models.FloatField(null=True)
	is_pg_percentage = models.IntegerField(null=True)
	roll_no = models.CharField(max_length=50,null=True)
	backlogs= models.IntegerField(null=True)
	current_backlogs = models.IntegerField(null=True)
	degree = models.CharField(max_length=50,null=True)
	work_experience= models.IntegerField(null=True)

class courses(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

	c_id = models.UUIDField(primary_key=True)
	c_name	= models.CharField(max_length=50,null=True)


class course_modules(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
	# id = models.AutoField(primary_key=True, default=1)
	c_id = models.ForeignKey("courses",on_delete=models.CASCADE,default=None,null=True)
	c_name	= models.CharField(max_length=50,null=True)
	Module_name = models.CharField(max_length=50,null=True)






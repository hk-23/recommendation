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
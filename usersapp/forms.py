from django import forms
from .models import User

class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput())
	password = forms.CharField(widget=forms.PasswordInput())

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email']

	#validating the email
	def clean_email(self):
		email = self.cleaned_data.get('email').lower()
		return email

	# #validating the mobile no
	# def clean_mobile(self):
	# 	mobile = self.cleaned_data.get('mobile')
	# 	if not len(mobile)==10:
	# 		raise forms.ValidationError('Enter a valid Mobile Number')
	# 	return mobile
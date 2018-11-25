from django import forms
from django.core import validators
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

#Wesh ma geule 
class UserForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')

#def check_for_z(value):
	#if value[0] != 'z':
		#raise forms.ValidationError('Name needs to start xith "Z" zdeuupp')


		#email = all_clean_data['email']
		#verify_email = all_clean_data['verify_email']

		#if email != verify_email:
			#raise forms.ValidationError('Make sure emails match')

# class NewTweetForm(forms.ModelForm):
# 	class Meta:
# 		model = Tweet
# 		fields = ['text']


# class NewTweetSpeForm(forms.ModelForm):
# 	class Meta:
# 		model = Tweet
# 		fields = '__all__'

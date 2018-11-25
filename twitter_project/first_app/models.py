from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	bio = models.CharField(max_length=400)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return (self.user.username)

class Tweet(models.Model):
	text = models.CharField(max_length= 140)
	date = models.DateField()
	# user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __repr__(self):
		return '<Text {}>'.format(self.text)

	def __str__(self):
		return self.text


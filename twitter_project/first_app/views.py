from django.shortcuts import render, redirect
from first_app.models import Tweet
from first_app.forms import UserForm, UserProfileInfoForm
import datetime


def gets_lasts_tweets(n=20):
	pass
	# lasts_tweets ={
	# 'list' : Tweet.objects.all().order_by('-date')[:n]
	# } 
	# return lasts_tweets

def gets_all_tweets_of_user(user_id):
	pass
	# all_tweets ={
	# 'list' : Tweet.objects.filter(user =user_id)
	# } 
	# return all_tweets

# Create your views here
def index(request):
	pass
	# return render(request, 'index.html',context=gets_lasts_tweets())

def profile(request,user_id):
	pass
	# return render(request, 'profile.html',context=gets_all_tweets_of_user(user_id))

def signup(request):
	registered = False
	if request.method =='POST':
		user_form = UserForm(data= request.POST) 
		profile_form = UserProfileInfoForm(data= request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit= False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()
			registered = True


		else : 
			print(user_form.errors, profile_form.errors)

	else: 
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'signup.html', context = {
		'user_form' : user_form,
		'profile_form' : profile_form, 
		'registered': registered
		})

def form_tweet_view(request):
 	pass
# 	form = forms.NewTweetForm()
# 	if request.method =='POST':
# 		form = forms.NewTweetForm(request.POST)
# 		if form.is_valid():
# 			form.save(commit=True)
# 			return index(request)
# 		else:
# 			print('Error - form is invalid')

# 	return render(request, 'form.html', {'form': form})


def create_tweet(request, user_id):
	pass
# 	user = User.objects.get(id = user_id)
# 	form = forms.NewTweetForm()
# 	if request.method =='POST':
# 		form = forms.NewTweetForm(request.POST)
# 		if form.is_valid():
# 			text = form.cleaned_data['text']
# 			tweet = Tweet(text= text, user=user, date=datetime.datetime.now())
# 			tweet.save()
# 			return redirect('/first_app/')

# 	return render(request, 'tweetform.html', {'form': form, 'user':user})

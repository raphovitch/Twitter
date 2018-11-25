import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_project.settings')

import django
django.setup()

# Fake populate script
import random
from faker import Faker
from first_app.models import User, Tweet, UserProfileInfo

fakegen = Faker()


def populate_user(N=100):
	for entry in range(N):
		# Create fake data for the entry

		user_fake_username = fakegen.user_name()
		user_fake_email = fakegen.safe_email()
		user_fake_password = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

		user = User.objects.get_or_create(username=user_fake_username, email=user_fake_email, password=user_fake_password)[0]

		user_profile_fake_bio = fakegen.text()
		user_profile = UserProfileInfo.objects.get_or_create(user= user, bio=user_profile_fake_bio)

		for tweet in range(20):

				tweet_fake_text = fakegen.text(max_nb_chars=400)
				tweet_fake_date = fakegen.date()


				# Create the fake webpage entry
				tweet = Tweet.objects.get_or_create(text=tweet_fake_text, date= tweet_fake_date)[0]



if __name__ =='__main__':
	print('Startiing to populate....')
	populate_user(100)
	print('Finished populating!')



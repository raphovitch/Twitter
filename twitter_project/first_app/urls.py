from django.contrib import admin
from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    # path('formuserpage/', views.form_user_view, name='form_user'),
    path('formtweetpage/', views.form_tweet_view, name='form_tweet'),
    path('profile/<int:user_id>/tweet', views.create_tweet, name='create_tweet'),
]

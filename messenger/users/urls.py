from django.contrib import admin
from django.urls import path
from users.views import profile
from users.views import contacts

urlpatterns = [
    path('<int:profile_id>/', profile, name='profile'),
    path('<int:profile_id>/contacts/', contacts, name='contacts'),
]

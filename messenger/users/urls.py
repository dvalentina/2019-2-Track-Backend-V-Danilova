from django.contrib import admin
from django.urls import path
from users.views import get_profile, get_contacts, search_profile

urlpatterns = [
    path('<int:profile_id>/', get_profile, name='profile'),
    path('<int:profile_id>/contacts/', get_contacts, name='contacts'),
    path('search/<str:user_name>/', search_profile, name='search profile'),
]

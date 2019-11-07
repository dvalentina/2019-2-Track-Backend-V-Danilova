from django.contrib import admin
from django.urls import path
from user.views import profile
from user.views import contact_list

urlpatterns = [
    path('<int:id>', profile, name='profile'),
    path('contact_list/<int:id>', contact_list, name='contact_list'),
]

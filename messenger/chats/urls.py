from django.contrib import admin
from django.urls import path
from chats.views import list
from chats.views import detail

urlpatterns = [
    path('<int:profile_id>/list/', list, name='list'),
    path('<int:chat_id>/', detail, name='detail'),
]

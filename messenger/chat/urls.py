from django.contrib import admin
from django.urls import path
from chat.views import chat_list
from chat.views import chat_detail

urlpatterns = [
    path('chat_list/<int:id>/', chat_list, name='chat_list'),
    path('<int:id>/', chat_detail, name='chat_detail'),
]

from django.contrib import admin
from django.urls import path
from chats.views import get_list, get_detail, create_personal_chat, ChatViewSet
from message.views import get_message_list, read_message, send_message, MessageViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'chats_drf', ChatViewSet)
router.register(r'chats_drf', MessageViewSet)

urlpatterns = [
    path('list/', get_list, name='list'),
    path('<int:chat_id>/', get_detail, name='detail'),
    path('<int:chat_id>/messages/', get_message_list, name='messages'),
    path('new_chat/', create_personal_chat, name='create chat'),
    path('read_message/', read_message, name='read message'),
    path('send_message/', send_message, name='send message'),
] + router.urls

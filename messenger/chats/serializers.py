from rest_framework import serializers
from chats.models import Chat, Member

class СhatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'is_group_chat', 'topic')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user', 'chat')

class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('chat')

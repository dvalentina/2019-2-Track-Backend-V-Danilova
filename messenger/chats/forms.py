from django.shortcuts import get_object_or_404
from django import forms
from chats.models import Chat, Member

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'chat']

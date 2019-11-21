from django import forms
from chats.models import Chat, Member

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['user', 'is_group_chat', 'topic']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        field = ['user', 'chat']

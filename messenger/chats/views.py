from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Member
from users.models import User

def detail(request, chat_id):
    if "GET" == request.method:
        print(chat_id)
        return JsonResponse({'CHAT DETAIL': ''})
    return HttpResponseNotAllowed(['GET'])

def list(request, profile_id):
    if "GET" == request.method:
        list = Chat.objects.all()
        list = list.filter(user_id=profile_id)
        return JsonResponse({'CHAT LIST': ''})
    return HttpResponseNotAllowed(['GET'])

def create_personal_chat(request):
    if "POST" == request.method:
        user_id = request.POST.get('user_id', False)
        if user_id is False:
            return HttpResponseBadRequest

        user = User.objects.get(id=user_id)
        is_group_chat = request.POST.get('is_group_chat', False)
        topic = request.POST.get('topic')

        chat = Chat.objects.create(is_group_chat=is_group_chat, topic=topic)
        member = Member.objects.create(user=user, chat=chat, new_messages=0)
        return JsonResponse({})
    return HttpResponseNotAllowed(['POST'])

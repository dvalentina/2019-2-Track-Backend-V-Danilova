from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound
from chats.models import Chat, Member
from users.models import User
from chats.forms import ChatForm

def get_detail(request, chat_id):
    if "GET" == request.method:
        chat = get_object_or_404(Chat, id=chat_id)
        return JsonResponse({
            'data': {'id': chat.id, 'topic': chat.topic}
            })
    return HttpResponseNotAllowed(['GET'])

def get_list(request, user_id):
    if "GET" == request.method:
        chats = Chat.objects.filter(user=user_id).values(
            'id', 'topic', 'is_group_chat'
        )
        return JsonResponse({'data': list(chats)})
    return HttpResponseNotAllowed(['GET'])

def create_personal_chat(request):
    if "POST" == request.method:
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return JsonResponse({
                'msg': 'Новый чат успешно создан',
                'id': chat.id,
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from message.models import Message
from chats.models import Member
from message.forms import MessageForm
from chats.forms import MemberForm

@login_required
def read_message(request):
    if "POST" == request.method:
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
        
            messages = Message.objects.filter(chat=member.chat).order_by('-added_at')
            last_message = messages.first()

            member.last_read_message_id = last_message.id
            member.new_messages = 0
            member.save()
            return JsonResponse({
                'data': {'member id': member.id, 'last read message': member.last_read_message_id}
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['GET'])

# @login_required
def send_message(request):
    if "POST" == request.method:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return JsonResponse({
                'msg': 'Сообщение отправлено',
                'id': message.id,
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

# @login_required
def get_message_list(request, chat_id):
    if "GET" == request.method:
        messages = Message.objects.values('chat', 'user', 'content', 'added_at')
        messages = messages.filter(chat=chat_id)
        return JsonResponse({'messages': list(messages)})
    return HttpResponseNotAllowed(['GET'])

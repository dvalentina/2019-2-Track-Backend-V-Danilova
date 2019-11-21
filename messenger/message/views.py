from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound
from message.models import Message
from chats.models import Member
from message.forms import MessageForm

def read_message(request):
    if "POST" == request.method:
        form = MemberForm(request.POST)
        member_id = request.POST.get('member_id', False)
        if member_id is False:
            return HttpResponseBadRequest
            
        try:
            member = Member.objects.get(id=member_id)
        except Member.DoesNotExist:
            return HttpResponseNotFound

        messages = Message.objects.all()
        messages = messages.filter(chat=member.chat)
        messages = messages.order_by('-added_at')
        last_message = messages.last()

        member.last_read_message = last_message
        return JsonResponse({})
    return HttpResponseNotAllowed(['GET'])

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

def get_message_list(request, chat_id):
    if "GET" == request.method:
        messages = Message.objects.all()
        messages = messages.filter(chat=chat_id)
        return JsonResponse({})
    return HttpResponseNotAllowed(['GET'])

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from message.models import Message
from chats.models import Member
from users.models import User
from message.forms import MessageForm
from chats.forms import MemberForm
from message.serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from cent import Client

@csrf_exempt
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
@csrf_exempt
def send_message(request):
    if "POST" == request.method:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            CentrifugeClient.publish(message)
            return JsonResponse({
                'msg': 'Сообщение отправлено',
                'id': message.id,
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

# @login_required
@cache_page(60 * 15)
def get_message_list(request, chat_id):
    if "GET" == request.method:
        messages = Message.objects.values('chat', 'user', 'content', 'added_at')
        messages = messages.filter(chat=chat_id)
        return JsonResponse({'messages': list(messages)})
    return HttpResponseNotAllowed(['GET'])

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def read_message(self, request):
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            messages = self.get_queryset()
            messages = messages.filter(chat=member.chat).order_by('-added_at')
            last_message = messages.first()

            member.last_read_message_id = last_message.id
            member.new_messages = 0
            member.save()
            serializer = self.get_serializer(messages, many=True)
            return Response(serializer.data)
        return JsonResponse({'errors': form.errors}, status=400)

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def send_message(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            CentrifugeClient.publish(message)
            serializer = self.get_serializer(message, many=False)
            return Response(serializer.data)
        return JsonResponse({'errors': form.errors}, status=400)
    
    @cache_page(60 * 15)
    @action(detail=False, methods=['get'])
    def get_message_list(self, request, chat_id):
        messages = self.get_queryset()
        messages = messages.filter(chat=chat_id)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

class CentrifugeClient:
    url = 'http://localhost:8001'
    api_key = '19cfcd36-a643-4989-a288-0a2e0f662d86'
    channel = "chats:centrifuge"
    client = Client(url, api_key, timeout=1)

    @classmethod
    def publish(cls, message):
        user = User.objects.get(id=message.user_id)
        data = {
            "status": "ok",
            "message": {
                'id': message.id,
                'user_id': message.user_id,
                'username': user.username,
                'content': message.content,
            }
        }
        cls.client.publish(cls.channel, data)

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from chats.models import Chat, Member
from chats.serializers import СhatSerializer, ChatListSerializer
from users.models import User
from chats.forms import ChatForm

@login_required
def get_detail(request, chat_id):
    if "GET" == request.method:
        chat = get_object_or_404(Chat, id=chat_id)
        return JsonResponse({
            'data': {'id': chat.id, 'topic': chat.topic}
            })
    return HttpResponseNotAllowed(['GET'])

@login_required
def get_list(request):
    user_id = request.user.id
    if "GET" == request.method:
        members = Member.objects.filter(user=user_id)
        chats = members.values('chat')
        return JsonResponse({'data': list(chats)})
    return HttpResponseNotAllowed(['GET'])

@login_required
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

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = СhatSerializer

    @action(detail=False, methods=['get'])
    def get_detail(self, request, chat_id):
        chat = self.get_queryset()
        chat = get_object_or_404(chat, id=chat_id)
        serializer = self.get_serializer(chat, many=False)
        return Response({"chats": serializer.data})

    @action(detail=False, methods=['get'])
    def get_list(self, request):
        user_id = request.user.id
        member = Member.objects.filter(user=user_id)
        serializer = ChatListSerializer(member, many=True)
        return Response({"chats": serializer.data})

    @action(detail=False, methods=['post'])
    def create_personal_chat(self, request):
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            serializer = self.get_serializer(chat, many=False)
            return Response({"chat": serializer.data})
        return JsonResponse({'errors': form.errors}, status=400)

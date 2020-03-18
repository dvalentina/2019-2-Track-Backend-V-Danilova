from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from chats.models import Chat, Member
from chat.serializers import ChatSerializer
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

class ChatView(APIView):
    def get(self,request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response({"chats": serializer.data})

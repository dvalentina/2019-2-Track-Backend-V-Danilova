from django.shortcuts import render
from django.http import JsonResponse

def chat_detail(request, id):
    if "GET" == request.method:
        try:
            chat_id = request.GET.get('chat_id')
            print(chat_id)
            #chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            raise Http404
        return JsonResponse({'CHAT DETAIL': 'TRUE', 'detail': 'some detail'})
    else:
        raise Http405

def chat_list(request, id):
    if "GET" == request.method:
        try:
            profile_id = request.GET.get('profile_id')
            #chat_list = ChatList.objects.get(id=profile_id)
        except ChatList.DoesNotExist:
            raise Http404
        return JsonResponse({'CHAT LIST': 'TRUE', 'first chat': 'Masha', 'second chat': 'Sasha'})
    else:
        raise Http405 


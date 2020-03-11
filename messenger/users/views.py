from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import User
from users.forms import UserForm

@login_required
def get_profile(request, profile_id):
    if "GET" == request.method:
        profile = User.objects.values('id', 'username', 'name', 'nick', 'avatar')
        profile = get_object_or_404(profile, id=profile_id)
        return JsonResponse({'PROFILE': profile})
    return HttpResponseNotAllowed(['GET'])

@login_required
def get_contacts(request, profile_id):
    if not request.user.id == profile_id:
        return HttpResponseForbidden
    if "GET" == request.method:
        return JsonResponse({'CONTACT LIST': 'TRUE', 'contact_1': 'Masha', 'contact_2': 'Sasha'})
    return HttpResponseNotAllowed(['GET'])

@login_required
def search_profile(request, nick):
    if "GET" == request.method:
        profiles = User.objects.filter(Q(name__contains=nick) | Q(nick__contains=nick)).values(
            'id', 'username', 'name', 'nick'
        )
        return JsonResponse({'Users': list(profiles)})
    return HttpResponseNotAllowed(['GET'])

def create_user(request):
    if "POST" == request.method:
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return JsonResponse({
                'msg': 'Пользователь создан',
                'id': new_user.id,
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

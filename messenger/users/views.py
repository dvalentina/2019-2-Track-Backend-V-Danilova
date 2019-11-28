from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from users.models import User

def get_profile(request, profile_id):
    if "GET" == request.method:
        profile = User.objects.values('id', 'name', 'nick', 'avatar')
        profile = get_object_or_404(profile, id=profile_id)
        return JsonResponse({'PROFILE': profile})
    return HttpResponseNotAllowed(['GET'])

def get_contacts(request, profile_id):
    if "GET" == request.method:
        return JsonResponse({'CONTACT LIST': 'TRUE', 'contact_1': 'Masha', 'contact_2': 'Sasha'})
    return HttpResponseNotAllowed(['GET'])

def search_profile(request, user_name):
    if "GET" == request.method:
        profiles = User.objects.filter(name__contains=user_name).values(
            'id', 'name', 'nick', 'avatar'
        )
        return JsonResponse({'Users': list(profiles)})
    return HttpResponseNotAllowed(['GET'])

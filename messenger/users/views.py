from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from users.models import User

def profile(request, profile_id):
    if "GET" == request.method:
        return JsonResponse({'PROFILE': 'TRUE','name': 'Ivan', 'surname': 'Ivanov'})
    return HttpResponseNotAllowed(['GET'])

def contacts(request, profile_id):
    if "GET" == request.method:
        return JsonResponse({'CONTACT LIST': 'TRUE', 'contact_1': 'Masha', 'contact_2': 'Sasha'})
    return HttpResponseNotAllowed(['GET'])

def search_profile(request, user_name):
    if "GET" == request.method:
        profile = User.objects.all()
        profile = profile.filter(name__contains=user_name)
        return JsonResponse({})
    return HttpResponseNotAllowed(['GET'])

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def profile(request, id):
    if "GET" == request.method:
        try:
            profile_id = request.GET.get('profile_id')
            #profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            raise Http404
        return JsonResponse({'PROFILE': 'TRUE','name': 'Ivan', 'surname': 'Ivanov'})
    else:
        raise Http405

def contact_list(request, id):
    if "GET" == request.method:
        try:
            profile_id = request.GET.get('profile_id')
            #contact_list = ContactList.objects.get(id=profile_id)
        except ContactList.DoesNotExist:
            raise Http404
        return JsonResponse({'CONTACT LIST': 'TRUE', 'contact_1': 'Masha', 'contact_2': 'Sasha'})
    else:
        raise Http405

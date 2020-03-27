from django.contrib import admin
from django.urls import path
from users.views import get_profile, get_contacts, search_profile, create_user, UserViewSet
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

urlpatterns = [
    path('<int:profile_id>/', get_profile, name='profile'),
    path('<int:profile_id>/contacts/', get_contacts, name='contacts'),
    path('search/<str:nick>/', search_profile, name='search profile'),
    path('create/', csrf_exempt(create_user), name='create user'),
]

router = routers.SimpleRouter()
router.register(r'users_drf', UserViewSet)
urlpatterns = router.urls

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    username = models.CharField(max_length=32, verbose_name='пользователь')
    name = models.CharField(max_length=32, verbose_name='имя пользователя', default='some name')
    nick = models.CharField(max_length=16, verbose_name='никнейм пользователя', default='some nick')
    avatar = models.TextField(verbose_name='аватар пользователя', default='some avatar')
    
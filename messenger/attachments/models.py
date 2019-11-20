from django.db import models

class Attachement(models.Model):
    class Meta:
        verbose_name = 'вложение'
        verbose_name_plural = 'вложения'
        
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
        verbose_name='чат, в котором содержится вложение',
        )
    message = models.ForeignKey(
        'message.Message',
        on_delete=models.CASCADE,
        verbose_name='сообщение, в котором содержится вложение',
        )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='пользователь, создавший вложение',
        )
    type = models.CharField(max_length=16, verbose_name='тип вложения')
    url = models.TextField(verbose_name='ссылка на вложение')

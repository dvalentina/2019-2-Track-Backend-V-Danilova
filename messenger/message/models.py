from django.db import models

class Message(models.Model):
    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['-added_at']
        
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
        verbose_name='чат, в котором содержится сообщение',
        )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='пользователь, отправивший сообщение',
        )
    content = models.TextField(verbose_name='текст сообщения')
    added_at = models.DateTimeField(
        null=False,
        auto_now=True,
        verbose_name='время отправки сообщения',
        )

from django.db import models

class Chat(models.Model):
    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'
        
    is_group_chat = models.BooleanField(
        default=False,
        verbose_name='является ли групповым чатом',
        )
    topic = models.CharField(max_length=32, verbose_name='тема чата')
    last_message = models.TextField(verbose_name='последнее сообщение')

class Member(models.Model):
    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'
        
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='пользователь, являющийся участником',
        )
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        verbose_name='чат, в котором состоит участник',
        )
    new_messages = models.IntegerField()
    last_read_message = models.ForeignKey('message.Message', on_delete=models.PROTECT)

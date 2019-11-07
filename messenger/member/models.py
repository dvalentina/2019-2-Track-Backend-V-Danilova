from django.db import models

class Member(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    chat = models.ForeignKey('chat.Chat', on_delete=models.DO_NOTHING)
    new_messages = models.IntegerField()
    last_read_message = models.ManyToManyField('message.Message')
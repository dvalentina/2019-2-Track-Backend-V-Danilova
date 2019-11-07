from django.db import models

class Message(models.Model):
    chat = models.ForeignKey('chat.Chat', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    content = models.TextField()
    added_at = models.DateTimeField()

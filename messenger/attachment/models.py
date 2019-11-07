from django.db import models

class Attachement(models.Model):
    chat = models.ForeignKey('chat.Chat', on_delete=models.DO_NOTHING)
    message = models.ForeignKey('message.Message', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=16)
    url = models.TextField()

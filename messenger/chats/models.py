from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=32)
    last_message = models.TextField()

class Member(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    new_messages = models.IntegerField()
    last_read_message = models.ForeignKey('Message', on_delete=models.PROTECT)

class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    added_at = models.DateTimeField()

class Attachement(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=16)
    url = models.TextField()

import json
from django.test import TestCase, Client
from django.urls import reverse
from message.factories import SequenceMessagesFactory
from message.models import Message
from users.models import User
from chats.models import Chat, Member

class MessageTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.first_user = User.objects.create(username='Test User N1', nick='greatNickname')
        self.second_user = User.objects.create(username='Test User N2', name='greatname')

        self.client.force_login(self.first_user)

        self.chat = Chat.objects.create(is_group_chat=False, topic='test topic')
        self.first_member = Member.objects.create(user_id=self.first_user.id, chat_id=self.chat.id, new_messages=0)
        self.second_member = Member.objects.create(user_id=self.second_user.id, chat_id=self.chat.id, new_messages=0)

        self.first_message = SequenceMessagesFactory.build(chat_id=self.chat.id, user_id=self.first_user.id)
        self.first_message.save()
        self.second_message = SequenceMessagesFactory.build(chat_id=self.chat.id, user_id=self.first_user.id)
        self.second_message.save()

    def test_read_message(self):
        response = self.client.post(reverse('read message'), {'user': self.first_user.id, 'chat': self.chat.id})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertGreaterEqual(content['data']['last read message'], 1)

    def test_send_message(self):
        response = self.client.post(reverse('send message'), {'user': self.first_user.id, 'chat': self.chat.id, 'content': 'test send message'})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'Сообщение отправлено')

    def test_get_message_list(self):
        response = self.client.get(reverse('messages', kwargs={'chat_id': self.chat.id}))
        self.assertTrue(response.status_code == 200)
        self.assertRaises(UnicodeDecodeError)
        self.assertJSONNotEqual(response.content, {'messages': []})
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), 2)

    def tearDown(self):
        print('messages test done')
    

import json
from django.test import TestCase, Client
from message.factories import SequenceMessagesFactory
from message.models import Message
from users.models import User
from chats.models import Chat, Member

class MessageTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.first_user = User.objects.create(id=1, username='Test User N1', nick='greatNickname')
        self.first_user.save()
        self.second_user = User.objects.create(id=2, username='Test User N2', name='greatname')
        self.second_user.save()

        self.client.force_login(self.first_user)

        self.chat = Chat.objects.create(id=0, is_group_chat=False, topic='test topic')
        self.chat.save()
        self.first_member = Member.objects.create(user_id=1, chat_id=0, new_messages=0)
        self.first_member.save()
        self.second_member = Member.objects.create(user_id=2, chat_id=0, new_messages=0)
        self.second_member.save()

        self.first_message = SequenceMessagesFactory.build()
        self.first_message.save()
        self.second_message = SequenceMessagesFactory.build()
        self.second_message.save()

    def test_read_message(self):
        response = self.client.post('/chats/read_message/', {'user': 1, 'chat': 0})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertGreaterEqual(content['data']['last read message'], 1)

    def test_send_message(self):
        response = self.client.post('/chats/send_message/', {'user': 1, 'chat': 0, 'content': 'test send message'})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'Сообщение отправлено')

    def test_get_message_list(self):
        response = self.client.get('/chats/0/messages/')
        self.assertTrue(response.status_code == 200)
        self.assertRaises(UnicodeDecodeError)
        self.assertJSONNotEqual(response.content, {'messages': []})
        content = json.loads(response.content)
        self.assertEqual(len(content['messages']), 2)

    def tearDown(self):
        print('I am done')
    

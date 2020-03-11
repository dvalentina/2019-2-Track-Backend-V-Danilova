import json
from django.test import TestCase, Client
from chats.models import Chat, Member
from users.models import User

class ChatsTest(TestCase):

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

    def test_create_personal_chat(self):
        response = self.client.post('/chats/new_chat/', {'topic': 'create chat test topic', 'is_group_chat': False})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'Новый чат успешно создан')

    def test_get_list(self):
        response = self.client.get('/chats/list/')
        self.assertFalse(response.status_code == 404)
        self.assertTrue(response.status_code == 200)
        self.assertJSONEqual(response.content, '{"data": [{"chat": 0}]}')

    def test_get_detail(self):
        response = self.client.get('/chats/0/')
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['data'], {'id': 0, 'topic': 'test topic'})
    
    def tearDown(self):
        print('I am done')
    
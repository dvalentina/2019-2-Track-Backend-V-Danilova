import json
from django.test import TestCase, Client
from django.urls import reverse
from chats.models import Chat, Member
from users.models import User

class ChatsTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.first_user = User.objects.create(username='Test User N1', nick='greatNickname')
        self.second_user = User.objects.create(username='Test User N2', name='greatname')

        self.client.force_login(self.first_user)

        self.chat = Chat.objects.create(is_group_chat=False, topic='test topic')
        self.first_member = Member.objects.create(user_id=self.first_user.id, chat_id=self.chat.id, new_messages=0)
        self.second_member = Member.objects.create(user_id=self.second_user.id, chat_id=self.chat.id, new_messages=0)

    def test_create_personal_chat(self):
        response = self.client.post(reverse('create chat'), {'topic': 'create chat test topic', 'is_group_chat': False})
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'Новый чат успешно создан')

    def test_get_list(self):
        response = self.client.get(reverse('list'))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['data'][0]['chat'], self.chat.id)

    def test_get_detail(self):
        response = self.client.get(reverse('detail', kwargs={'chat_id': self.chat.id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['data'], {'id': self.chat.id, 'topic': 'test topic'})
    
    def tearDown(self):
        print('chats test done')
    
import json
from django.test import TestCase, Client
from users.models import User

class UsersTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.first_user = User.objects.create(id=1, username='Test User N1', nick='greatNickname')
        self.first_user.save()
        self.second_user = User.objects.create(id=2, username='Test User N2', name='greatname')
        self.second_user.save()

        self.client.force_login(self.first_user)

    def test_get_profile(self):
        response = self.client.get('/users/1/')
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['PROFILE']['username'], 'Test User N1')

    def test_get_contacts(self):
        response = self.client.get('/users/1/contacts/')
        self.assertTrue(response.status_code == 200)
        self.assertJSONNotEqual(response.content, '{}')

    def test_search_profile(self):
        response = self.client.get('/users/search/great/')
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['Users'][0]['name'], 'greatname')
        self.assertEqual(content['Users'][0]['username'], 'Test User N2')
        self.assertEqual(content['Users'][1]['nick'], 'greatNickname')
        self.assertEqual(content['Users'][1]['username'], 'Test User N1')
        self.assertNotEqual(content['Users'][1]['name'], '')

    def tearDown(self):
        print('I am done')
    
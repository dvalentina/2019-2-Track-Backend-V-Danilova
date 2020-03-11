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
    
from selenium import webdriver

class SeleniumTest(TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.webdriver = webdriver.Chrome(chrome_options=chrome_options)
        self.webdriver.implicitly_wait(10)
        self.webdriver.get('http://localhost:8000/users/0/')

    def test_login(self):    
        elem = self.webdriver.find_element_by_link_text('Login with GitHub')
        assert elem is not None
        elem.click()

    def tearDown(self):
        self.webdriver.close()

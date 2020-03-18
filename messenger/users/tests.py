import json
from django.test import TestCase, Client
from django.urls import reverse
from mock import patch
from users.models import User

class UsersTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.first_user = User.objects.create(username='Test User N1', nick='greatNickname')
        self.second_user = User.objects.create(username='Test User N2', name='greatname')

        self.client.force_login(self.first_user)

    def test_get_profile(self):
        response = self.client.get(reverse('profile', kwargs={'profile_id': self.first_user.id}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['PROFILE']['username'], 'Test User N1')

    def test_get_contacts(self):
        response = self.client.get(reverse('contacts', kwargs={'profile_id': self.first_user.id}))
        self.assertTrue(response.status_code == 200)
        self.assertJSONNotEqual(response.content, '{}')

    def test_search_profile(self):
        response = self.client.get(reverse('search profile', kwargs={'nick': 'great'}))
        self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content['Users'][0]['name'], 'greatname')
        self.assertEqual(content['Users'][0]['username'], 'Test User N2')
        self.assertEqual(content['Users'][1]['nick'], 'greatNickname')
        self.assertEqual(content['Users'][1]['username'], 'Test User N1')
        self.assertNotEqual(content['Users'][1]['name'], '')

    @patch('users.views.create_user')
    def test_create_user(self, create_user_mock):
        create_user_mock()
        self.assertTrue(create_user_mock.called)

    def tearDown(self):
        print('users test done')
    
from selenium import webdriver

class SeleniumTest(TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.webdriver = webdriver.Chrome(chrome_options=chrome_options)
        self.webdriver.implicitly_wait(10)
        self.webdriver.get('http://localhost:8000/users/0/')

    def test_login(self):    
        elem = self.webdriver.find_element_by_xpath('/html/body/p/a')
        assert elem is not None
        elem.click()
        login_form = self.webdriver.find_element_by_xpath('//*[@id="login_field"]')
        assert login_form is not None
        password_form = self.webdriver.find_element_by_xpath('//*[@id="password"]')
        assert password_form is not None
        login_form.send_keys('username')
        password_form.send_keys('password')
        sign_in_button = self.webdriver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[9]')
        assert sign_in_button is not None
        sign_in_button.click()
        failed_login_p = self.webdriver.find_element_by_xpath('//*[@id="login"]/p')
        assert failed_login_p is not None

    def tearDown(self):
        self.webdriver.close()
        print('selenium test done')

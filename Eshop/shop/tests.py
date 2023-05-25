from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import connection

class SelfTest(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/register.html')


    def test_contact_page(self):
       response = self.client.get(reverse('contact'))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'contact.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/login.html')

    





# class SecurityTest(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_xss_security(self):
#         # Create a test user
#         username = 'testuser'
#         password = 'testpassword'
#         self.client.post(reverse('register'), {'username': user_form.username, 'password': password})

#         # Craft a malicious payload
#         payload = '<script>alert("XSS Attack!");</script>'

#         # Send a POST request to a vulnerable endpoint with the payload
#         response = self.client.post(reverse('vulnerable_endpoint'), {'data': payload})

#         # Assert that the payload is properly sanitized
#         self.assertNotContains(response, payload)
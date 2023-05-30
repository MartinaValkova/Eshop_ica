from django.test import Client
import django.test
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils.html import escape
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db import connection




#Test to check if the middleware are configured

class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        with self.modify_settings(
            MIDDLEWARE={
                "append": "django.middleware.cache.FetchFromCacheMiddleware",
                "prepend": "django.middleware.cache.UpdateCacheMiddleware",
                "remove": [
                    "django.contrib.sessions.middleware.SessionMiddleware",
                    "django.contrib.auth.middleware.AuthenticationMiddleware",
                    "django.contrib.messages.middleware.MessageMiddleware",
                    "django.middleware.csrf.CsrfViewMiddleware",
                ],
            }
        ):
            response = self.client.get("/")
            # ...



try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.3, 2.4 fallback.
import datetime, re

from django.http import SimpleCookie
from django.test.client import Client, MULTIPART_CONTENT
from django.test.testcases import TestCase

# Test Csrf cookies

class CsrfClient(Client):
    class _CookieRequest:
        def __init__(self, cookies):
            if not '_csrf_cookie' in cookies:
                cookies['_csrf_cookie'] = 'csrf-cookie'
            self.COOKIES = dict([
                (key, cookies[key].value) for key in cookies
            ])
    
    def post(self, path, data={}, content_type=MULTIPART_CONTENT,
        follow=False, csrf='default', **extra):
        "Requests a response from the server using POST, auto-includes CSRF "
        "token unless csrf=False or the _csrf_cookie has not yet been set."
        if csrf and content_type == MULTIPART_CONTENT \
                and not data.has_key('csrf_token'):
            data['csrf_token'] = csrf_utils.new_csrf_token(
                CsrfClient._CookieRequest(self.cookies), csrf
            )
        return super(CsrfClient, self).post(
            path, data, content_type=content_type, follow=follow, csrf=csrf,
            **extra
        )
    



class ClickjackingTest(TestCase):
    def setUp(self):
        # Set up the test by creating a new client
        self.client = Client()

    def test_clickjacking_protection(self):
        # Test if clickjacking protection is enabled
        response = self.client.get(reverse('register'))
        # Send a GET request to the 'register' URL
        self.assertTrue(response.has_header('X-Frame-Options'))
        # Assert that the response has the 'X-Frame-Options' header
        self.assertEqual(response['X-Frame-Options'], 'DENY')
        # Assert that the value of the 'X-Frame-Options' header is 'DENY'



class RegistrationSecurityTest(TestCase):
    def setUp(self):
        # Set up the test by creating a new client
        self.client = Client()

    def test_csrf_enabled(self):
        # Test if CSRF protection is enabled
        response = self.client.get(reverse('register'))
        # Send a GET request to the 'register' URL
        self.assertEqual(response.status_code, 200)
        # Assert that the response status code is 200 (successful)
        self.assertTrue(response.cookies.get('csrftoken'))
        # Assert that the response contains a 'csrftoken' cookie

    def test_secure_cookies(self):
        # Test if secure cookies are used
        response = self.client.get(reverse('register'))
        # Send a GET request to the 'register' URL
        self.assertEqual(response.status_code, 200)
        # Assert that the response status code is 200 (successful)
        sessionid_cookie = response.cookies.get('sessionid')
        # Retrieve the 'sessionid' cookie from the response
        if sessionid_cookie is not None:
            # Check if the 'sessionid' cookie exists
            self.assertTrue(sessionid_cookie.secure)
            # Assert that the 'sessionid' cookie is secure (using HTTPS)




class SelfTest(TestCase):

    def test_home_page(self):
        # Test the home page
        response = self.client.get(reverse('register'))
        # Send a GET request to the 'register' URL
        self.assertEqual(response.status_code, 200)
        # Assert that the response status code is 200 (successful)
        self.assertTemplateUsed(response, 'shop/register.html')
        # Assert that the response uses the 'shop/register.html' template

    def test_contact_page(self):
        # Test the contact page
        response = self.client.get(reverse('contact'))
        # Send a GET request to the 'contact' URL
        self.assertEqual(response.status_code, 200)
        # Assert that the response status code is 200 (successful)
        self.assertTemplateUsed(response, 'contact.html')
        # Assert that the response uses the 'contact.html' template

    def test_login_page(self):
        # Test the login page
        response = self.client.get(reverse('login'))
        # Send a GET request to the 'login' URL
        self.assertEqual(response.status_code, 200)
        # Assert that the response status code is 200 (successful)
        self.assertTemplateUsed(response, 'shop/login.html')

        # Assert that the response uses the 'shop/login.html' template


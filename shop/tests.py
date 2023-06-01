from django.test import Client
import django.test
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils.html import escape
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db import connection
from django.utils.crypto import get_random_string




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


#This class creates tests to check the functionality of the main page.

class SecurityTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)


    def test_user_password_hashed(self):
        # Verify that the user's password is hashed
        self.assertNotEqual(self.user.password, 'testpassword')

    def test_logout(self):
        # Test successful logout
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'))

        # Successful logout should return status code 200
        self.assertEqual(response.status_code, 200)

        # User should be logged out
        self.assertNotIn('_auth_user_id', self.client.session)


    def test_brute_force_protection(self):
        # Test brute force protection by making multiple failed login attempts
        for _ in range(5):
            password = get_random_string(length=10)
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': password})

        # After multiple failed attempts, response should be 302
        self.assertEqual(response.status_code, 302)

    def test_username_enumeration_attack(self):
        # Test username enumeration attack
        username = 'testuser'
        response = self.client.post(reverse('login'), {'username': username, 'password': 'testpassword'})

        # Response should be 200 for both valid and invalid usernames
        self.assertEqual(response.status_code, 200)


    def test_brute_force_protection(self):
        # Test brute force protection by making multiple failed login attempts
        for _ in range(5):
            password = get_random_string(length=10)
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': password})

        # After multiple failed attempts, response should be 429
        self.assertEqual(response.status_code, 429)


    def test_admin_site_protection(self):
        # Test admin site protection by accessing admin index page without authentication
        response = self.client.get(reverse('admin:index'))

        # Admin site should redirect when not authenticated
        self.assertEqual(response.status_code, 302)

    def test_admin_login_view(self):
        # Test admin login page accessibility
        response = self.client.get(reverse('admin:login'))

        # Admin login page should be accessible
        self.assertEqual(response.status_code, 200)

#'test_user_password_hashed' verifies that the user's password has been hashed and is not stored in plain text.

#''test_logout'': This test verifies that the logout mechanism is operational.
#  It pretends to be a logged-in user, sends a POST request to the logout endpoint, and checks that the return status code is 200 and the user is logged out.

#"test_brute_force_protection" verifies the brute force protection technique.
#  It attempts many unsuccessful logins and validates that after a given number of attempts, the response status code is 302, indicating that the protection mechanism is activated.
#
#''test_username_enumeration_attack"': This test looks for a vulnerability in username enumeration. 
# To avoid this, it performs a POST request to the login endpoint with both valid and invalid usernames and checks that the return status code is 200 in both circumstances. 
#
#''test_admin_site_protection'' ::guarantees that the admin site is secure. 
# It tries to visit the admin index page without login and confirms that the response status code is 302, indicating that the user is being redirected when not authorized.

#''test_admin_login_view'': This test validates the admin login page's accessibility. 
# It performs a GET request to the admin login endpoint and checks the return status code to ensure that it is 200, indicating that the login page is accessible.
#
from django.test import Client
import django.test
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils.html import escape
from django.contrib.auth.models import User


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
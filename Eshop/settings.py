"""
Django settings for Eshop project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url
import environ
import os.path  
import sys



env = environ.Env()
environ.Env.read_env()

load_dotenv()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    "shop",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "captcha",
    'axes',
    
    
]


# reCAPTCHA keys
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "axes.middleware.AxesMiddleware",
    
   
]

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

#Settings for deployment

# CSRF Protection

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# Protection against XSS attacks 
SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENCT_TYPE_NOSNIFF = True

#Enable HSTS

SECURE_HSTS_SECONDS = 86400

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Django CSP configuration

CSP_DEFAULT_SRC = ("'none'",)
CSP_SCRIPT_SRC = ["https://stackpath.bootstrapcdn.com",
    "https://cdn.jsdelivr.net",
    "https://code.jquery.com"
    ]

CSP_STYLE_SRC = ["https://stackpath.bootstrapcdn.com"]
CSP_IMG_SRC = ("'self'",)
CSP_FRAME_SRC = ["https://docs.google.com"]












ROOT_URLCONF = "Eshop.urls"




TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'shop', 'templates', 'shop'),
                 ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Eshop.wsgi.application"




# Database which was used in development
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
    #"default": {
       # "ENGINE": "django.db.backends.sqlite3",
       # "NAME": BASE_DIR / "db.sqlite3",
    #}
#}




# Render PostgreSQL database used for deployment

DATABASES = {

    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
    
    }


 #Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRT = [
    BASE_DIR / 'static'
]



MEDIA_URL = '/media/'





# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = 'index'

LOGIN_URL = 'login'


# axes configuration settings

AXES_FAILURE_LIMIT:3 # How many times a user can fail login

AXES_COOLOFF_TIME:1 # Wait 1 hours before attempting to login again

AXES_RESET_ON_SUCCESS = True  # Reset failed login attempts

AXES_LOCKOUT_TEMPLATE = 'accountLocked.html'
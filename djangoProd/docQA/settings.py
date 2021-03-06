"""
Django settings for docQA project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

#session expire hours
TIMESESSIONEXPIRE = 6000

#URL docQA
URL='http://145.239.156.90:5000/'


# STMP server for confirmation email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@palo-it.com'
EMAIL_HOST_PASSWORD = 'Paloitfrance2018!'
EMAIL_PORT = 587

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Google recaptcha
GOOGLE_RECAPTCHA_SECRET_KEY = '6Ld2uE8UAAAAAEFvgup-rWAWw3-9ZpOtVLiJfHl0'


#Google analytics django-otto-admin
OA_ANALYTICS_CREDENTIALS_JSON = BASE_DIR
OA_ANALYTICS_VIEW_ID =0

LOGIN_REDIRECT_URL = 'get_question'
LOGOUT_REDIRECT_URL = 'home'

AUTH_PROFILE_MODULE = 'engineResults.UserProfile'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-b^#@=b6@n5l&af$h8517ohnhtf3@1i41o43qa_=_epb2be+be'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['145.239.156.90', 'localhost', '127.0.0.1', '0.0.0.0', 'gdpr.palo-it.com']


# Application definition

INSTALLED_APPS = [
    'otto_admin',
    'users',
    'templates',
    'engineResults.apps.EngineresultsConfig',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'gunicorn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'docQA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)
STATICFILES_DIRS = [
    #os.path.join(os.path.dirname(BASE_DIR), 'docQAWebSite/templates/static'),
    #normpath(join(BASE_DIR, 'assets')),
    #'/usr/local/lib/python3.6/site-packages/django/contrib/admin/static',
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'docQAWebSite/templates/static')
STATIC_URL = '/static/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'docQA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'doc_qa',
        'USER': 'doc_qa',
        'PASSWORD': 'doc_qa_pwd',
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#User model creat on users app
AUTH_USER_MODEL = 'users.CustomUser'

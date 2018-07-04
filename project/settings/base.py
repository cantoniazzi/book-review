# -*- coding: utf-8 -*-

import os

from django.conf.locale.pt_BR import formats

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(
	os.path.abspath(__file__)), os.pardir))

BASE_PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

INSTALLED_APPS = [
	# django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third apps
    'rest_framework',

    # project apps
    'project.apps.books',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Date and Time

DATETIME_FORMAT = 'd/m/Y \à\s H:i'

formats.DATETIME_FORMAT = DATETIME_FORMAT

DATE_FORMAT = 'd/m/Y'

formats.DATE_FORMAT = DATE_FORMAT

DATE_INPUT_FORMATS = ['%d/%m/%y', '%d/%m/%Y', '%Y-%m-%d']

TIME_FORMAT = 'H:i'

formats.TIME_FORMAT = TIME_FORMAT

TIME_INPUT_FORMATS = ['%H:%M']


STATICFILES_DIRS = []

STATIC_ROOT = os.path.join(BASE_DIR, '../resources/static/')

STATIC_URL = '/static/'

# GOOD READS API
GOOD_READS_API_KEY = os.getenv('GOOD_READS_API_KEY', '')
GOOD_READS_API_SECRET = os.getenv('GOOD_READS_API_SECRET', '')

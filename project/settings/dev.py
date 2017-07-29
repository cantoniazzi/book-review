# -*- coding: utf-8 -*-

from .base import *


# General
# https://docs.djangoproject.com/en/1.11/topics/settings/
# https://docs.djangoproject.com/en/1.11/ref/settings/

ENV = 'dev'

SECRET_KEY = '3xn3alr=cmqsqwim^b*ru!gq)japcela&&ofcsuzhr$ms+vl9-'

DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_URL = 'http://localhost:8000'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../database/db.sqlite3'),
    }
}
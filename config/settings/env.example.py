from .base import *

SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []
    

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
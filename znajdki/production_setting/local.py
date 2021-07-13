from .base import *

DEBUG = config('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'znajdki',
        'USER': 'aleo',
        'PASSWORD': 'aleo',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
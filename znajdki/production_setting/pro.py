from .base import *

DEBUG = False

ADMINS = (
    ('aleo', 'aleksander.wiedenski.praca@gmail.com'),
)
ALLOWED_HOSTS = ['znajdki.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'znajdkii',
        'USER': 'aleo',
        'PASSWORD': 'aleo',
    }
}
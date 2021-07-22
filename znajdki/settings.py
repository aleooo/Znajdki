from pathlib import Path
import os
from decouple import config


# PROJECT_PATH = Path(__file__).resolve().parent.parent
# PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__))))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'poszukiwania.apps.PoszukiwaniaConfig',
    "bootstrap5",
    'autoslug',
    'rest_framework',
    'django.contrib.admin',
    'rosetta'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'znajdki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'znajdki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('pl', 'Polski'),
)
LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/staticfiles/'
# STATICFILES = os.path.join(PROJECT_PATH, 'poszukiwania/staticfiles/')
STATIC_ROOT = os.path.join(PROJECT_PATH, '../static')
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'image')


LOGIN_REDIRECT_URL = 'poszukiwania:objects_list'
LOGOUT_REDIRECT_URL = 'poszukiwania:login'
LOGIN_URL = 'poszukiwania:login'
LOGOUT_URL = 'poszukiwania:logout'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'katalog.poszukiwacza@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CATALOG_SESSION_ID = 'catalog'

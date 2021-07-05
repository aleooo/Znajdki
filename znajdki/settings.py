from pathlib import Path
import os
from utils.misc import get_git_changeset
from decouple import config


#BASE_DIR = Path(__file__).resolve().parent.parent
# PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__))))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'poszukiwania.apps.PoszukiwaniaConfig',
    "bootstrap5",
    'djgeojson',
    'leaflet',
    'autoslug',
    'django.contrib.gis',
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
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'znajdki',
        'USER': 'aleo',
        'PASSWORD': 'aleo',
        'HOST': '127.0.0.1',
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
    ('en', 'english'),
    ('pl', 'polski'),
)
LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES = os.path.join(PROJECT_PATH, 'static/')
STAATIC_ROOT = '/static/'
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'image')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'image/')

GOOGLE_MAPS_API_KEY = 'AIzaSyAxQ0RZR4xPvmfR-1D8I-cU3PyeKRwvfLI'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

LOGIN_REDIRECT_URL = 'poszukiwania:objects_list'
LOGOUT_REDIRECT_URL = 'poszukiwania:login'
LOGIN_URL = 'poszukiwania:login'
LOGOUT_URL = 'poszukiwania:logout'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'katalog.poszukiwacza@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
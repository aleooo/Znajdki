from pathlib import Path
import os
from utils.misc import get_git_changeset


#BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SECRET_KEY = '^7f$lqi((jk52j=#zkx$k7x^nlnvk5%tqjxd6s6q8$-0p0va^-'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'poszukiwania.apps.PoszukiwaniaConfig',
    'django_extensions',
    'mapa.apps.MapaConfig',
    'bootstrapform',
    'djgeojson',
    'leaflet',

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
#STATIC_URL = "/static/%s/" % get_git_changeset(PROJECT_PATH)
#STATICFILES = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'image/')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'image/')

GOOGLE_MAPS_API_KEY = 'AIzaSyAxQ0RZR4xPvmfR-1D8I-cU3PyeKRwvfLI'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (52.013, 21.93),
    'DEFAULT_ZOOM': 13,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'DEFAULT_PRECISION': 6,
}
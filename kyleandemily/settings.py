"""
Django settings for kyleandemily project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import envdir
import warnings
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from photologue import PHOTOLOGUE_APP_DIR

ENVDIR_PATH = os.environ.get('ENVDIR_PATH')
if ENVDIR_PATH and os.path.isdir(ENVDIR_PATH):
    envdir.open(ENVDIR_PATH)
else:
    warnings.warn('Unable to find ENVDIR_PATH: {0}'.format(ENVDIR_PATH))

APP_ENV = os.environ.get('APP_ENV', 'local')
PROJECT_ROOT = os.environ.get('PROJECT_ROOT', None)
if PROJECT_ROOT is None:
    PROJECT_ROOT = PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
else:
    PROJECT_ROOT = os.path.abspath(PROJECT_ROOT)
    PROJECT_DIR = os.path.join(PROJECT_ROOT, 'app')
DB_ROOT = os.path.join(PROJECT_ROOT, 'db')
GOOGLE_SITE_VERIFICATION = os.environ.get('GOOGLE_SITE_VERIFICATION', '')

SECRET_KEY = os.environ.get('SECRET_KEY', APP_ENV)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'donotreply8386@gmail.com'
DEFAULT_TO_EMAIL = 'buschang.rockman.wedding@gmail.com'

ALLOWED_HOSTS = ['www.kyleandemily.com',
                 'kyleandemily.com',
                 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'default.db'),
    },
    'rsvp_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'rsvp.db'),
    },
}

DATABASE_ROUTERS = [
    'kyleandemily.rsvp.db_router.RSVPRouter',
]

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://guest:guest@localhost:5672//')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'photologue',
    'south',
    'sortedm2m',
    #'wamp',

    'kyleandemily.wedding',
    'kyleandemily.base',
    'kyleandemily.rsvp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS = (
    PHOTOLOGUE_APP_DIR,
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'kyleandemily.processor.wedding_default',
)

ROOT_URLCONF = 'kyleandemily.urls'

WSGI_APPLICATION = 'kyleandemily.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

if APP_ENV == "local":
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    STATIC_URL = 'http://' + APP_ENV + '.static.kyleandemily.com/'
    MEDIA_URL = 'http://' + APP_ENV + '.media.kyleandemily.com/'

if APP_ENV == "prod":
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {
        'dsn': os.environ.get('RAVEN_CONFIG_DSN', ''),
    }
if APP_ENV != "prod":
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG = True
    TEMPLATE_DEBUG = True

try:
    from kyleandemily.local_settings import *
except ImportError:
    pass


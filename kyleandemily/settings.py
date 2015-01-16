"""
Django settings for kyleandemily project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
import os
APP_ENV = os.environ.get('APP_ENV', 'local')
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
REMOTE_ROOT = '/usr/local/kyleandemily'

if APP_ENV == "local":
    DB_ROOT = PROJECT_DIR
else:
    DB_ROOT = os.path.join(REMOTE_ROOT, 'db_' + APP_ENV)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(PROJECT_DIR, 'key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
if APP_ENV != "prod":
    DEBUG = True
    TEMPLATE_DEBUG = True


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donotreply8386@gmail.com'
EMAIL_HOST_PASSWORD = 'password8386'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ALLOWED_HOSTS = ['www.kyleandemily.com',
                 'kyleandemily.com',
                 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'default.db'),
    },
    #'wamp_db': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(DB_ROOT, 'wamp.db'),
    #},
    'wedding_photo_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'wedding_photo.db'),
    },
    'rsvp_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_ROOT, 'rsvp.db'),
    },
}

DATABASE_ROUTERS = [
    'kyleandemily.wedding.db_router.PhotologueRouter',
    'kyleandemily.rsvp.db_router.RSVPRouter',
    #'wamp.db_router.WampRouter',
]


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
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
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

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
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

if APP_ENV == "local":
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
else:
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    MEDIA_ROOT = os.path.join(REMOTE_ROOT, 'media_' + APP_ENV)
    STATIC_URL = 'http://' + APP_ENV + '.static.kyleandemily.com/'
    MEDIA_URL = 'http://' + APP_ENV + '.media.kyleandemily.com/'



from photologue import PHOTOLOGUE_APP_DIR
TEMPLATE_DIRS = (
    PHOTOLOGUE_APP_DIR,
)

if APP_ENV == "prod":
    RAVEN_CONFIG = {
        'dsn': 'http://8e93f45b82f34f629cbd65ab129f2f08:80de27c57bba414096b01881bd9e5b65@sentry.rocktavious.com/2',
    }
else:
    RAVEN_CONFIG = {
        'dsn': 'http://d23b2be3932b441a95ead317bbcaa192:9f2d380f50a14ee48cde6f88099cad15@sentry.rocktavious.com/4',
    }

DEBUG_TOOLBAR_PATCH_SETTINGS = False

try:
    from kyleandemily.local_settings import *
except ImportError:
    pass


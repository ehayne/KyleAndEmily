"""
WSGI config for kyleandemily project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys

activate_this = '/Users/zoeserver/.pyenv/versions/kyleandemily/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kyleandemily.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

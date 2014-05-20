"""
WSGI config for kyleandemily project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
exec_file('~/.pyenv/versions/ohrockman/bin/activate_this.py')

import os
import sys
sys.path.append('/Volumes/STORAGE/Web/kyleandemily')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kyleandemily.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

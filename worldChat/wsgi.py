"""
WSGI config for worldChat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.get('DJANGO_SETTINGS_MODULE', 'worldChat.settings')

application = get_wsgi_application()

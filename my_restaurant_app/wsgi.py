"""
WSGI config for my_restaurant_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import config
ENVIROMENT_DEVELOPMENT = config('DEVELOPMENT', cast=bool)

if ENVIROMENT_DEVELOPMENT:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'my_restaurant_app.settings_dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'my_restaurant_app.settings')

application = get_wsgi_application()

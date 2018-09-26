"""
WSGI config for coffeet3ch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffeet3ch.settings')

#application = Cling(get_wsgi_application())

application = get_wsgi_application()
application = WhiteNoise(application)
#application.add_files('/path/to/more/static/files', prefix='more-files/')

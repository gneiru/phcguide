"""
<<<<<<<< HEAD:health/wsgi.py
WSGI config for health project.
========
WSGI config for user_management project.
>>>>>>>> parent of 0478e96 (Initial):user_management/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<<< HEAD:health/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
>>>>>>>> parent of 0478e96 (Initial):user_management/wsgi.py

application = get_wsgi_application()

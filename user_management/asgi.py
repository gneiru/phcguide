"""
<<<<<<<< HEAD:health/asgi.py
ASGI config for health project.
========
ASGI config for user_management project.
>>>>>>>> parent of 0478e96 (Initial):user_management/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:health/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
>>>>>>>> parent of 0478e96 (Initial):user_management/asgi.py

application = get_asgi_application()

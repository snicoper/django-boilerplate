#!/usr/bin/env python
# flake8: noqa
# Para pruebas rápidas, similar a ./manage.py shell

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings.local')

import django
django.setup()
####################################################################################################
from django.conf import settings

print(settings.AUTH_USER_MODEL)

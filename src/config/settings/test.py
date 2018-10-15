# flake8: noqa
from .local import *

# Añadir ~/tests a PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(BASE_DIR), 'tests'))

# Application definition
INSTALLED_APPS += ()

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.test.sqlite3'),
    }
}

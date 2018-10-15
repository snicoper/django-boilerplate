from django.conf import settings

UPLOAD_TO = getattr(settings, 'UPLOAD_TO', 'accounts/profiles')

DEFAULT_PHOTO = getattr(settings, 'DEFAULT_PHOTO', 'accounts/profiles/user.png')

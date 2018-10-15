from django.db.models import manager
from django.utils import timezone
from django.utils.crypto import get_random_string

from . import settings as auth_settings


class RegisterUserManager(manager.Manager):

    def move_user_tmp_to_users(self, user_model, user_temp):
        """Mueve un usuario temporal a la tabla User y elimina el usuario temporal."""
        new_user = user_model.objects.create(
            username=user_temp.username,
            email=user_temp.email,
            password=user_temp.password
        )
        if new_user:
            user_temp.delete()

    def delete_expired_users_temp(self):
        """Elimina registros expirados."""
        days = auth_settings.AUTH_REGISTER_EXPIRE_DAYS
        diff = timezone.now() - timezone.timedelta(days=days)
        self.filter(date_joined__lt=diff).delete()


class UserEmailUpdateManager(manager.Manager):

    def generate_unique_token(self):
        while True:
            token = get_random_string(length=30)
            if not self.filter(token=token):
                return token

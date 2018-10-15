from django.db import models


class ContactManager(models.Manager):

    def contact_messages_unread(self):
        """Contar numero de mensajes sin leer."""
        return self.filter(has_read=False).count()

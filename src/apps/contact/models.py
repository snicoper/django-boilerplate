from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.mixins.models import TimeStampedModel

from .managers import ContactManager


class Contact(TimeStampedModel):
    email = models.EmailField(
        verbose_name=_('Email')
    )
    subject = models.CharField(
        verbose_name=_('Asunto'),
        max_length=255
    )
    text = models.TextField(
        verbose_name=_('Mensaje')
    )
    is_register = models.BooleanField(
        verbose_name=_('Usuario registrado')
    )
    has_read = models.BooleanField(
        verbose_name=_('Mensaje leído'),
        default=False
    )

    objects = ContactManager()

    def __str__(self):
        return self.subject[0:30]

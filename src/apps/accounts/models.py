import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from utils.images import ImageResize

from . import settings as user_settings


class User(AbstractUser):
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=150,
        blank=True
    )
    photo = models.ImageField(
        verbose_name=_('Foto'),
        upload_to=user_settings.UPLOAD_TO,
        blank=True
    )

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_photo = self.photo

    def save(self, *args, **kwargs):
        photo_has_changed = False
        self.slug = slugify(self.username)
        if self.photo.name != self._original_photo.name:
            photo_has_changed = True
            if self._original_photo.name != user_settings.DEFAULT_PHOTO:
                if os.path.exists(self._original_photo.path):
                    os.remove(self._original_photo.path)
        if not self.photo:
            self.photo.name = user_settings.DEFAULT_PHOTO
        super().save(*args, **kwargs)
        self._original_photo = self.photo
        if photo_has_changed and self.photo.name != user_settings.DEFAULT_PHOTO:
            image_resize = ImageResize(self.photo.path)
            image_resize.resize(self.photo.path, 150, 150)

    def get_absolute_url(self):
        return reverse('accounts:profile')

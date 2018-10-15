from django.conf import settings
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin,
)
from django.shortcuts import Http404, redirect


class AnonymousRequiredMixin(object):
    """Mixin para autorizar solo a usuarios anónimos.

    Si no es un usuario anónimo, lo redirecciona a la pagina LOGIN_REDIRECT_URL.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


class PermissionRequiredOr404Mixin(PermissionRequiredMixin):
    """Si no tiene permisos lanzara Http404."""

    def handle_no_permission(self):
        raise Http404


class IsCurrentUserOwnerOr404Mixin(LoginRequiredMixin):
    """Solo el owner y superuser puede ver la view.

    Requiere de un campo 'owner_field', que sera el campo a comprobar.
    Por defecto owner_field = 'owner'.
    """
    owner_field = 'owner'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        obj_owner = getattr(obj, self.owner_field)
        if not obj_owner:
            raise NotImplementedError(f'El campo {self.owner_field} no existe')
        user = request.user
        if not obj_owner == user and not user.is_superuser:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

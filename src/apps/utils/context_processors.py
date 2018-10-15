from django.conf import settings
from django.contrib.sites.models import Site

from contact.models import Contact


def global_template_vars(request):
    """Variables comunes en los templates."""
    context = {
        'SITE': Site.objects.get_current(),
        'DEBUG': settings.DEBUG
    }
    # Administrador
    if request.user.is_superuser:
        context['CONTACT_MESSAGES_UNREAD'] = Contact.objects.contact_messages_unread()
    return context

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from utils.http import get_full_path
from utils.mail import send_templated_mail


def notify_new_contact_message(request, contact):
    """Envía una notificación del formulario de contacto."""
    site = get_current_site(request)
    site_name = site.name
    subject = f'Nuevo email de contacto en {site_name}'
    context = {
        'is_register': contact.is_register,
        'subject': contact.subject,
        'email': contact.email,
        'text': contact.text,
        'site_name': site_name,
        'callback_url': get_full_path(request, 'contact:details', pk=contact.pk)
    }
    send_templated_mail(
        subject=subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipients=settings.GROUP_EMAILS['CONTACTS'],
        context=context,
        template_text='contact/emails/contact.txt'
    )

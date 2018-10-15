from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from utils.mixins.views import PermissionRequiredOr404Mixin

from .emails import notify_new_contact_message
from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def get_initial(self):
        initial = super().get_initial()
        initial['is_register'] = False
        if self.request.user.is_authenticated:
            initial['email'] = self.request.user.email
            initial['is_register'] = True
        return initial

    def get_success_url(self):
        notify_new_contact_message(self.request, self.object)
        msg_success = 'Se ha enviado el mensaje correctamente'
        messages.success(self.request, msg_success)
        return reverse('home_page')


class ContactListView(LoginRequiredMixin, PermissionRequiredOr404Mixin, ListView):
    template_name = 'contact/list.html'
    permission_required = 'contact.can_view'
    model = Contact


class ContactDetailView(LoginRequiredMixin, PermissionRequiredOr404Mixin, DetailView):
    template_name = 'contact/detail.html'
    permission_required = 'contact.can_view'
    model = Contact

    def get(self, request, *args, **kwargs):
        """Actualizar el mensaje de contacto como leído."""
        Contact.objects.filter(pk=kwargs['pk']).update(has_read=True)
        return super().get(request, *args, **kwargs)


class ContactDeleteView(LoginRequiredMixin, PermissionRequiredOr404Mixin, DeleteView):
    template_name = 'contact/delete.html'
    permission_required = 'contact.can_delete'
    model = Contact

    def get_success_url(self):
        messages.success(self.request, 'Mensaje eliminado con éxito')
        return reverse('contact:list')

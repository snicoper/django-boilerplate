from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView

from accounts.forms import PhotoUpdateForm

from .models import User


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/photo_update.html'
    form_class = PhotoUpdateForm
    model = User

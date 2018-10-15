from django import forms
from django.contrib.auth.forms import (
    UserChangeForm as AuthUserChangeForm,
    UserCreationForm as AuthUserCreationForm,
)

from .models import User


class UserChangeForm(AuthUserChangeForm):
    """Form para editar usuario en admin."""

    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserCreationForm(AuthUserCreationForm):
    """Form creación de usuarios."""

    class Meta(AuthUserCreationForm.Meta):
        model = User


class PhotoUpdateForm(forms.ModelForm):
    restore_photo = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = User
        fields = ('photo',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        restore_photo = self.cleaned_data.get('restore_photo')
        if restore_photo:
            instance.photo = None
        if commit:
            instance.save()
        return instance

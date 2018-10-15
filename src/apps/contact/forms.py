from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Formulario de contacto."""

    class Meta:
        model = Contact
        fields = ('email', 'subject', 'text', 'is_register')
        widgets = {
            'is_register': forms.HiddenInput
        }

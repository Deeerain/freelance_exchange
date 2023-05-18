from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _


USER_MODEL = get_user_model()


class ReplayFrom(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = USER_MODEL
        fields = ('username', 'email')

    def clean(self) -> Dict[str, Any]:
        data = super().clean()
        password = data.get('password')
        password_repeat = data.get('password_repeat')

        if not password == password_repeat:
            msg = _("Passwords don't match")
            self.add_error('password_repeat', msg)

        return data

from django.conf import settings

from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AbstractBaseUser
from django.views.generic import CreateView
from django.forms.models import BaseModelForm

from accounts.forms import RegistrationForm


USER_MODEL: AbstractBaseUser = get_user_model()


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    model = USER_MODEL
    form_class = RegistrationForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = USER_MODEL()
        user.username = form.cleaned_data.get('username')
        user.email = form.cleaned_data.get('email')
        user.set_password(form.cleaned_data.get('email'))
        user.save()

        login(self.request, user)

        return redirect(settings.LOGIN_REDIRECT_URL)

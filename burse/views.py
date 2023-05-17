from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.views import LoginView, LogoutView

from .models import Account
from .forms import RegistrationForm


USER_MODEL: AbstractBaseUser = get_user_model()


class HomeView(TemplateView):
    template_name = 'burse/index.html'


class Freelancers(ListView):
    model = Account
    template_name = 'freelancers/list.html'


class LoginView(LoginView):
    template_name = 'auth/login.html'


class LogoutView(LogoutView):
    template_name = 'auth/logout.html'


class RegistrationView(CreateView):
    template_name = 'auth/registration.html'
    model = USER_MODEL
    form_class = RegistrationForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = USER_MODEL()
        user.username = form.cleaned_data.get('username')
        user.email = form.cleaned_data.get('email')
        user.set_password(form.cleaned_data.get('email'))
        user.save()

        login(self.request, user)

        return redirect('tasks:list')

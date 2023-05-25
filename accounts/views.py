from typing import Any
from django.conf import settings
from django.db.models import Model, QuerySet

from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AbstractBaseUser
from django.views.generic import CreateView, DetailView, ListView
from django.forms.models import BaseModelForm

from accounts.forms import RegistrationForm

from tasks.models import Task
from replays.models import Replay


USER_MODEL: AbstractBaseUser = get_user_model()


class ProfileView(DetailView):
    model = USER_MODEL
    template_name = 'accounts/my_profile.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return get_object_or_404(self.model, pk=self.request.user.pk)    


class MyTasksView(ListView):
    model = Task
    template_name = 'accounts/my_tasks.html'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(employer=self.request.user)


class MyTaskView(DetailView):
    model = Task
    template_name = 'accounts/my_task.html'


class MyReplays(ListView):
    model = Replay
    template_name = 'accounts/my_replays.html'


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

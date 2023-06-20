from typing import Any
from django.conf import settings
from django.db.models import Model, QuerySet

from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AbstractBaseUser
from django.views.generic import CreateView, DetailView, ListView
from django.forms.models import BaseModelForm

from accounts.forms import RegistrationForm

from tasks.models import Task
from tasks import services as task_services
from replays.models import Replay

from accounts import services as account_services


USER_MODEL: AbstractBaseUser = get_user_model()


class ProfileView(DetailView):
    model = USER_MODEL
    template_name = 'accounts/my_profile.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        try:
            return account_services.get_user_by_pk(self.request.user.pk)
        except Model.DoesNotExist:
            return HttpResponseNotFound()


class MyTasksView(ListView):
    model = Task
    template_name = 'accounts/my_tasks.html'

    def get_queryset(self) -> QuerySet[Any]:
        return task_services.task_get_all_by_employer(self.request.user)


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
        try:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = account_services.user_register(username, email, password)

            login(self.request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        except account_services.UserAlreadyRegisteredError:
            return self.get(self.request, *self.args, **self.kwargs)

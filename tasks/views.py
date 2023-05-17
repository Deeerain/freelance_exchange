from typing import Any, Dict, Type
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse

from replays.models import Replay
from replays.forms import ReplayForm

from .models import Task
from .forms import CreateTaskForm


class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'tasks.add_task'
    login_url = 'burse:auth'
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/create.html'

    def get_form(self,
                 form_class: Type[BaseModelForm] | None = ...
                 ) -> BaseModelForm:

        return self.form_class(self.request.POST)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task = Task(**form.cleaned_data)
        task.employer = self.request.user
        task.save()

        return redirect(reverse('tasks:list'))


class TaksListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list.html'

    def get_queryset(self) -> QuerySet[Any]:
        objects = self.model.objects.filter(visible=True)

        if slug := self.kwargs.get('slug'):
            objects = objects.filter(slug=slug)

        [setattr(item, 'replay_count',
                 Replay.get_count_from_task(item)) for item in objects]

        return objects


class TaskDetailView(DetailView, ModelFormMixin):
    model = Task
    form_class = ReplayForm
    context_object_name = 'task'
    template_name = 'task/detail.html'

    def get_form(self,
                 form_class: Type[BaseModelForm] | None = ...
                 ) -> BaseModelForm:

        return self.form_class()

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> models.Model:
        return get_object_or_404(self.model, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        replays = Replay.objects.filter(task=self.get_object())
        context['replays'] = replays
        context['can_replay'] = replays.filter(user=self.request.user
                                               ).count() <= 0

        return context

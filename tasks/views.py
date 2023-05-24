from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from burse.views.mixins import SearchMixin

from replays.models import Replay
from replays.forms import ReplayForm

from .models import Task
from .forms import CreateTaskForm


class TaskCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'tasks.add_task'
    login_url = 'accounts:signin'
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/create.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task = Task(**form.cleaned_data)
        task.employer = self.request.user
        task.save()

        return redirect(reverse('tasks:list'))


class TaksListView(ListView, SearchMixin):
    model = Task
    template_name = 'task/list.html'
    search_fields = ['title', 'description']
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:

        filter_values = {}
        filter_values['visible'] = True

        if filter_value := self.kwargs.get('slug'):
            filter_values['categories__slug'] = filter_value

        return Task.objects.select_related('categories').annotate(
            replay_count=models.Count('replay')).filter(**filter_values)


class TaskDetailView(DetailView, ModelFormMixin):
    model = Task
    form_class = ReplayForm
    context_object_name = 'task'
    template_name = 'task/detail.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> models.Model:
        return get_object_or_404(self.model, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        replays = Replay.objects.filter(task=self.get_object())
        context['replays'] = replays
        context['can_replay'] = replays.filter(user=self.request.user
                                               ).count() <= 0

        return context

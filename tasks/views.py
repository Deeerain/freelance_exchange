from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from burse.views.mixins import SearchMixin
from replays.forms import ReplayForm

from .models import Task
from .forms import CreateTaskForm
from replays.models import Replay


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
            filter_values['category__slug'] = filter_value

        return Task.objects.select_related('category').annotate(
            replay_count=models.Count('replays')).filter(**filter_values)


class TaskDetailView(DetailView, ModelFormMixin):
    model = Task
    form_class = ReplayForm
    context_object_name = 'task'
    template_name = 'task/detail.html'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().prefetch_related('replays')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class TaskReplayView(View):
    def get(self, request, category_slug, slug):
        task = get_object_or_404(Task, slug=slug)
        can_replay = not Replay.objects.filter(
            user=self.request.user, task=task).exists()

        form = ReplayForm()

        return render(request, 'task/replay.html', {
            'object': task,
            'can_replay': can_replay,
            'form': form,
        })

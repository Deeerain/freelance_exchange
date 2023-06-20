from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from burse.views.mixins import SearchMixin
from replays.forms import ReplayForm

from tasks.models import Task
from tasks.forms import CreateTaskForm
from replays.models import Replay
from tasks import services as task_services


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    permission_required = 'tasks.add_task'
    login_url = 'accounts:signin'
    model = Task
    form_class = CreateTaskForm
    template_name = 'task/create.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_services.task_create(self.request.user, **form.cleaned_data)
        return redirect(reverse('tasks:list'))


class TaksListView(generic.ListView, SearchMixin):
    model = Task
    template_name = 'task/list.html'
    search_fields = ['title', 'description']
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        filter_values = {}
        filter_values['visible'] = True

        if filter_value := self.kwargs.get('slug'):
            filter_values['category__slug'] = filter_value

        return task_services.task_all(**filter_values)


class TaskDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Task
    form_class = ReplayForm
    context_object_name = 'task'
    template_name = 'task/detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.setdefault('form', self.get_form())

        return context

    def get_queryset(self) -> QuerySet[Any]:
        return task_services.task_all_with_replays()


class TaskReplayView(generic.View):
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

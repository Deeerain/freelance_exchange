from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse

from tasks.models import Task

from replays.forms import ReplayForm
from replays import services as replay_services


class ReplayCreateView(CreateView):
    model = Task
    form_class = ReplayForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_id = self.request.GET.get('task_id')
        task = get_object_or_404(self.model, pk=task_id)

        replay_services.create_replay(task=task, user=self.request.user,
                                      **form.changed_data)

        return redirect(reverse('tasks:detail', kwargs={
            'category_slug': task.category.slug, 'slug': task.slug}))

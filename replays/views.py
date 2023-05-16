from typing import Any, Type
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse

from tasks.models import Task

from .forms import ReplayForm
from .models import Replay


class ReplayCreateView(CreateView):
    model = Task
    form_class = ReplayForm

    def get_form(self, form_class: Type[BaseModelForm] | None = ...) -> BaseModelForm:
        return self.form_class(self.request.POST)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_id = self.request.GET.get('task_id')
        task = get_object_or_404(self.model, pk=task_id)

        replay = Replay()
        replay.task = task
        replay.user = self.request.user
        replay.commet = form.cleaned_data['comment']
        replay.save()

        return redirect(reverse('tasks:detail', kwargs={'category_slug': task.categories.slug, 'slug': task.slug}))

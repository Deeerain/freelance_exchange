from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from tasks.models import Task

from replays.forms import ReplayForm
from replays.models import Replay
from replays import services as replay_services


class ReplayCreateView(generic.edit.ModelFormMixin, generic.View):
    model = Replay
    form_class = ReplayForm

    def get_success_url(self) -> str:
        return self.request.headers.get('referer')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_id = self.request.GET.get('task_id')
        task = get_object_or_404(Task, pk=task_id)

        replay_services.create_replay(task=task, user=self.request.user,
                                      **form.changed_data)

        return super().form_valid(form)

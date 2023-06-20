from django.db import models

from tasks import models as task_models


def task_create(employer, **kwargs):
    task_models.Task.objects.create(employer=employer, **kwargs)


def task_all(**kwargs) -> models.QuerySet[task_models.Task]:
    return task_models.Task.objects.filter(**kwargs)


def task_all_with_info(**kwargs) -> models.QuerySet[task_models.Task]:
    return task_models.Task.objects.select_related('category')\
        .annotate(replay_count=models.Count('replays'))\
        .filter(**kwargs)


def task_all_with_replays(**kwargs):
    return task_all().prefetch_related('replays').filter(**kwargs)


def task_get_all_by_employer(employer):
    return task_all(employer=employer)

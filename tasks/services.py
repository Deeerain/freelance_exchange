from django.db.models import Count

from tasks import models


def task_create(employer, **kwargs):
    models.Task.objects.create(employer, **kwargs)


def task_all(**kwargs):
    return models.Task.objects.select_related('category')\
        .annotate(replay_count=Count('replays'))\
        .filter(**kwargs)


def task_get_all_by_employer(employer):
    return task_all(employer=employer)

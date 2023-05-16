from django.db import models
from django.contrib.auth import get_user_model

from tasks.models import Task


USER_MODEL = get_user_model()


class Replay(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    commet = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_count_from_task( task):
        return Replay.objects.filter(task=task).count()
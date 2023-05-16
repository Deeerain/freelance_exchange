from django.db import models
from burse.models import Account
from tasks.models import Task


OFFER_STATE = [
    (1, 'Ожидание'),
    (2, 'В работе'),
    (3, 'Закрыт'),
]


class Offer(models.Model):
    executor = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    state = models.TextField(choices=OFFER_STATE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
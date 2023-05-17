from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)


class User(AbstractUser):
    is_customer = models.ManyToManyField(Role, db_index=True)

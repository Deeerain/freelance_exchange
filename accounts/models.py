from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=30,
                            unique=True, db_index=True)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    roles = models.ManyToManyField(
        verbose_name=_('Roles'), to=Role, db_index=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self) -> str:
        return self.username

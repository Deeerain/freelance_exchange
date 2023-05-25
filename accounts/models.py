from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=30,
                            unique=True, db_index=True)

    class Meta:
        verbose_name = _('Роль')
        verbose_name_plural = _('Роли')

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    roles = models.ManyToManyField(
        verbose_name=_('Роли'), to=Role, db_index=True)

    description = models.TextField(_('Описание'), max_length=1000, blank=True)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self) -> str:
        return self.username

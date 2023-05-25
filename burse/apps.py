from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BurseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'burse'
    verbose_name = _('Биржа')

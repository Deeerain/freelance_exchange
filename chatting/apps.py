from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChattingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatting'
    verbose_name = _('Сообщения')

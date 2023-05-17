from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .managment import create_role


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self) -> None:
        post_migrate.connect(
            create_role,
        )

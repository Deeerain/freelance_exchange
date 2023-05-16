from django.apps import AppConfig


class BurseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'burse'

    def ready(self) -> None:
        from . import signals
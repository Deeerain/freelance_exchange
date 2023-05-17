from django.conf import settings
from django.apps import apps as global_apps
from django.db import DEFAULT_DB_ALIAS, router


def create_role(app_config, verbosity=2, interactive=True,
                using=DEFAULT_DB_ALIAS, apps=global_apps, **kwargs,):

    app_label = app_config.label
    try:
        app_config = apps.get_app_config(app_label)
        Role = apps.get_model("accounts", "Role")
    except LookupError:
        return

    if not router.allow_migrate_model(using, Role):
        return

    roles = settings.BURSE_ROLES

    for role in roles:
        Role.objects.get_or_create(name=role)

    if verbosity >= 2:
        for role in roles:
            print("Adding role '%s'" % role)
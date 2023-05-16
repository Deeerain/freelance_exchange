import logging

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .models import Account


logger = logging.getLogger(__name__)
USER_MODEL = get_user_model()



@receiver(post_save, sender=USER_MODEL)
def user_post_save_signal(sender, instance, **kwargs):
    Account.objects.get_or_create(user=instance)
    logger.info(f'Created Account for user: {instance.pk}')
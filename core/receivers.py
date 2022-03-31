from django.db.models.signals import post_save
from django.dispatch import receiver
from core import models, actions

@receiver(post_save, sender=models.State, dispatch_uid='save_log_file')
def save_log_file(instance: 'models.State', created: bool, kwargs):
    actions.StateActions.save_log_file(state=instance)
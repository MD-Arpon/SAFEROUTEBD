from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler that automatically generates or updates 
    a Profile record for every User.
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        # get_or_create prevents RelatedObjectDoesNotExist crashes
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()
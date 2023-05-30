from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Signal receiver function that creates a profile when a User object is saved
    if created:
        # Check if a new User instance is created
        Profile.objects.create(user=instance)
        # Create a new Profile instance associated with the User

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Signal receiver function that saves the profile when a User object is saved
    instance.profile.save()
    # Save the associated Profile instance for the User
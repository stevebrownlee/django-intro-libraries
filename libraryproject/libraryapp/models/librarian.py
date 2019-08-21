from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .library import Library


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Library, related_name="librarians",
        null=True,
        blank=True,
        on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_librarian(sender, instance, created, **kwargs):
    if created:
        Librarian.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_librarian(sender, instance, **kwargs):
    instance.librarian.save()

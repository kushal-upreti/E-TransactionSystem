from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from transactions.models import Wallet

@receiver(post_save, sender=UserProfile)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

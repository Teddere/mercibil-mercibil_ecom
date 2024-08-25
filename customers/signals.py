from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Shopper
from customers.models import Customer


@receiver(post_save, sender=Shopper)
def create_customer(sender, instance, created, **kwargs):
    if created and instance.role == "SHOPPER":
        Customer.objects.create(user=instance)

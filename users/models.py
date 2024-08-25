from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=200)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SHOPPER = "SHOPPER", "Shopper"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50,choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

class ShopperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results

class Shopper(User):
    base_role = User.base_role.SHOPPER

    shopper = ShopperManager()

    class Meta:
        proxy = True

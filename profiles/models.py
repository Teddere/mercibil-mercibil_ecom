from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Vendeur')
    bio = models.TextField(default='No Bio')
    avatar = models.ImageField(upload_to='profile/',default='profile/profile_no.svg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile de {self.user.username}"



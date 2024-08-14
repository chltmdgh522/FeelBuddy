import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique=True)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.CharField(max_length=10, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

#     def __str__(self):
#         return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def save(self, *args, **kwargs):
        if not self.nickname:
            random_names = ['화사한 유채꽃', '푸른 바다', '밝은 햇살', '고요한 달빛']
            self.nickname = random.choice(random_names)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
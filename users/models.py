import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def get_random_nickname(self):
        random_names = ['화사한 유채꽃', '푸른 바다', '밝은 햇살', '고요한 달빛']
        if self.nickname:
            return self.nickname
        else:
            return random.choice(random_names)

    def __str__(self):
        return self.user.username
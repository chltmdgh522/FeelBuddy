import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import re
from django.core.exceptions import ValidationError


def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9]+$', value):
        raise ValidationError('아이디는 영문자와 숫자만 사용할 수 있습니다.')
    
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_username],
        error_messages={
            'unique': "이미 사용 중인 아이디입니다.",
        },
    )


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
            random_names = ['화사한 유채꽃', '푸른 바다', '밝은 햇살', '고요한 달빛','필버디', '돼지와 함께 춤을']
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
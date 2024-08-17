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
            random_names = [
                '화사한 유채꽃',
                '푸른 바다',
                '밝은 햇살',
                '고요한 달빛',
                '필버디',
                '돼지와 함께 춤을',
                '마법사의 주문',
                '피자와 콜라의 전쟁',
                '구름 위의 트램펄린',
                '레몬으로 만든 로켓',
                '슈퍼히어로의 휴식처',
                '달콤한 초콜릿 폭풍',
                '햄버거의 비밀 파티',
                '시간 여행자의 소원',
                '고양이의 비밀 카페',
                '우주에서 온 보물상자',
                '치즈와 함께 춤추다',
                '버터플라이의 대모험',
                '별빛이 내린 저녁',
                '산 속의 비밀 레시피'
            ]

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

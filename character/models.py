from django.db import models

from users.models import User


# Create your models here.
# 사용자가 생성한 캐릭터 테이블
class AdminCharacter(models.Model):
    emotion = models.CharField(max_length=10)
    image = models.ImageField(upload_to='characters/img/')  #모델 변화 ---> 이미지 필드 추가

    def __str__(self):
        return self.emotion


class UserCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    adminCharacter = models.ForeignKey(AdminCharacter, on_delete=models.CASCADE)  # 초기 캐릭터 식별자
    introduce = models.TextField()  # 생성 이유
    trash = models.BooleanField(default=False)  # 캐릭터 휴지통 플래그
    name = models.CharField(max_length=30)  # 캐릭터 이름

    def __str__(self):
        return self.name
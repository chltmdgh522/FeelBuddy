from django.db import models

from users.models import User


# Create your models here.
# 사용자가 생성한 캐릭터 테이블
class UserCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자1
    AdminCharacter = models.ForeignKey(AdminCharacter, on_delete=models.CASCADE)  # 초기 캐릭터 식별자 즉 걸려있는데 5개이니깐 adminCharacter로 부터 외래키를 받아야됨
    introduce = models.TextField()  # 생성 이유 (사용자가 캐릭터 생성할 때 폼에서 작성하는 코멘트)
    trash = models.BooleanField(default=False)  # 캐릭터 휴지통 플래그
    name = models.CharField(max_length=30)  # 캐릭터 이름


class AdminCharacter(models.Model):
    emotion = models.CharField(max_length=10)

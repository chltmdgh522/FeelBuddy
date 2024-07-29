from django.db import models

from users.models import User


class Character(models.Model):
    user = models.CharField(max_length=255)  # 유저 식별자
    introduce = models.CharField(max_length=255)  # 생성 이유 (사용자가 캐릭터 생성할 때 폼에서 작성하는 코멘트)
    trash = models.BooleanField(default=False)  # 캐릭터 휴지통 플래그
    name = models.CharField(max_length=30)  # 캐릭터 이름


class ChatbotContent(models.Model):
    user = models.CharField(max_length=255)  # 유저 식별자
    character = models.ForeignKey(Character, on_delete=models.CASCADE)  # 챗봇 식별자
    ai_content = models.TextField()  # 인공지능 대화
    user_content = models.TextField()  # 사용자 대화
    time = models.DateField()  # 대화생성시간


class EmotionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    character = models.ForeignKey(Character, on_delete=models.CASCADE)  # 챗봇 식별자

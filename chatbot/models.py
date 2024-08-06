from django.db import models

from character.models import UserCharacter
from users.models import User


# 챗봇에서 사용자 대화 내용 기록 테이블
class ChatbotUserContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    userCharacter = models.ForeignKey(UserCharacter, on_delete=models.CASCADE)  # 유저가 생성한 캐릭터 식별자
    user_content = models.TextField()  # 사용자 대화
    time = models.DateTimeField(auto_now_add=True)  # 대화생성시간


# 챗봇에서 AI 대화 내용 기록 테이블
class ChatbotAIContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    userCharacter = models.ForeignKey(UserCharacter, on_delete=models.CASCADE)  # 유저가 생성한 캐릭터 식별자
    ai_content = models.TextField()  # 인공지능 대화
    time = models.DateTimeField(auto_now_add=True)  # 대화생성시간

# 감정 기록 로그(아마 대화양 즉 대화 건수)
class EmotionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    chatbotUserContent = models.ForeignKey(ChatbotUserContent, on_delete=models.CASCADE)  # 챗봇 유저 대화내용 식별자

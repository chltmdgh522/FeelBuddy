from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.
# 사용자가 생성한 캐릭터 테이블
# 감정과 이미지 파일의 매핑을 위한 상수 정의
EMOTION_CHOICES = [
    ('angry', 'Angry'),
    ('anxiety', 'Anxiety'),
    ('fear', 'Fear'),
    ('joy', 'Joy'),
    ('sad', 'Sad'),
]


class AdminCharacter(models.Model):
    emotion = models.CharField(max_length=10, choices=EMOTION_CHOICES, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

<<<<<<< HEAD
    def __str__(self):
        return self.emotion

    def save(self, *args, **kwargs):
        # 이미지 경로 설정에서 settings.MEDIA_URL 제거
        self.image = f"character/{self.emotion}.png"
        super(AdminCharacter, self).save(*args, **kwargs)
=======
>>>>>>> develop


class UserCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 식별자
    adminCharacter = models.ForeignKey(AdminCharacter, on_delete=models.CASCADE)  # 초기 캐릭터 식별자
    introduce = models.TextField()  # 생성 이유
    last_content = models.TextField(default=" ")  # 인공지능 마지막 대화
    trash = models.BooleanField(default=False)  # 캐릭터 휴지통 플래그
    name = models.CharField(max_length=30)  # 캐릭터 이름

    def __str__(self):
        return self.name

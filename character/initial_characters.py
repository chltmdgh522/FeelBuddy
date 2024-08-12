# initial_characters.py
import sys
import os

# 프로젝트 루트 디렉토리를 추가합니다.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Django 설정 로드
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from character.models import AdminCharacter #상대임포트 절대임포트로 변경
from django.conf import settings
import os

emotions = ['angry', 'anxiety', 'fear', 'joy', 'sad']
for emotion in emotions:
    image_path = f"character/{emotion}.png"
    image_full_path = os.path.join(settings.MEDIA_ROOT, image_path)
    if not AdminCharacter.objects.filter(emotion=emotion).exists():
        admin_character = AdminCharacter(emotion=emotion)
        with open(image_full_path, 'rb') as image_file:
            admin_character.image.save(image_path, image_file, save=True)

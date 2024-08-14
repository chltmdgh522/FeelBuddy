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

def create_initial_characters():
    emotions = ['angry', 'anxiety', 'fear', 'joy', 'sad']
    for emotion in emotions:
        image_path = f"{emotion}.png"
        AdminCharacter.objects.get_or_create(emotion=emotion, defaults={'image': image_path})

create_initial_characters()


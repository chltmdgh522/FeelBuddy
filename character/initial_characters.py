# initial_characters.py
from .models import AdminCharacter
from django.conf import settings

def create_initial_characters():
    emotions = ['angry', 'anxiety', 'fear', 'joy', 'sad']
    for emotion in emotions:
        image_path = f"{settings.MEDIA_URL}characters/{emotion}.png"
        AdminCharacter.objects.get_or_create(emotion=emotion, defaults={'image': image_path})

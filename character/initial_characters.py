# character/initial_characters.py
from character.models import AdminCharacter
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

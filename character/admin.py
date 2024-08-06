from django.contrib import admin

# Register your models here.
from django.contrib import admin

from character.models import UserCharacter, AdminCharacter

# Register your models here.
admin.site.register(UserCharacter)
admin.site.register(AdminCharacter)

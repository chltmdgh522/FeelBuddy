from django.contrib import admin

# Register your models here.
from django.contrib import admin

from chatbot.models import ChatbotUserContent, ChatbotAIContent, EmotionLog

# Register your models here.
admin.site.register(ChatbotUserContent)
admin.site.register(ChatbotAIContent)
admin.site.register(EmotionLog)

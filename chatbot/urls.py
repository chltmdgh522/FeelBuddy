from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'chatbot'
urlpatterns = [

    # AI 챗봇 관련 페이지
    # 여기서 핵심은 AJAX로 불러올거라서 대화내용을 개개인 마다 list url 설정해서 뭐 안해도됨

    path('chatbot/<int:pk>', chatbot_content_list, name='chatbot_content_list'),  # pk는 캐릭터의 식별자임 챗봇의 식별자 아님!!

    path('chatbot/ai/create/<int:pk>', chatbot_ai_create, name='chatbot_ai_create'),  # pk는 캐릭터의 식별자 유저는 세션에서 불러올거니깐

    path('chatbot/user/create/<int:pk>', chatbot_user_create, name='chatbot_user_create'),
    # pk는 캐릭터의 식별자 유저는 세션에서 불러올거니깐

    # 감정 기록 페이지
    path('emotion/', emotion, name='emotion'),
    path('weekly_emotion_log/', weekly_emotion_log, name='weekly_emotion_log'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'users'

urlpatterns = [

    # 메인
    path('', main, name='main'),

    # 회원
    path('signup.html/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

    #비밀번호 찾기
    path('password_reset/', password_reset_request, name='password_reset'), #비밀번호 재설정 요청 폼
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'), #새 비밀번호 설정 폼
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'), #비밀번호 재설정 완료 페이지
]

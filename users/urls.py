from django.urls import path
from .views import *
from django.conf import settings

app_name = 'users'

urlpatterns = [

    # 메인
    path('', main, name='main'),

    # 회원
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]

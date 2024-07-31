from django.shortcuts import render
from .models import UserCharacter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser # 로그인 기능없이 테스트를 해보기 위해서 

# Create your views here.

def character_list(request):
    if isinstance(request.user, AnonymousUser):
        user_characters = []  # 빈 리스트로 설정하거나 다른 처리를 할 수 있습니다.
    else:
        user_characters = UserCharacter.objects.filter(user=request.user)
    return render(request, 'character/character_list.html', {'user_characters': user_characters})

def character_create(request):
    return 0


def character_create_detail(request):
    return 0


def character_update(request):
    return 0


def trash_delete(request):
    return 0


def trash(request):
    return 0


def trash_restore(request):
    return 0

def trash_perfect_delete(request):
    return 0
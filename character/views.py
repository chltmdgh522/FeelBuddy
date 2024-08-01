from django.shortcuts import render, redirect, get_object_or_404
from .models import UserCharacter, AdminCharacter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser # 로그인 기능없이 테스트를 해보기 위해서 
from .forms import UserCharacterForm, AdminCharacterForm

# Create your views here.

def character_list(request):
    if isinstance(request.user, AnonymousUser):
        user_characters = []  # 빈 리스트로 설정하거나 다른 처리를 할 수 있습니다.
    else:
        user_characters = UserCharacter.objects.filter(user=request.user)
    return render(request, 'character/character_list.html', {'user_characters': user_characters})

def character_create(request):
    admin_characters = AdminCharacter.objects.all()  # 모든 AdminCharacter 가져오기
    return render(request, 'character/character_create.html', {'admin_characters': admin_characters})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdminCharacter
from .forms import UserCharacterForm

@login_required
def character_create_detail(request, pk):
    admin_character = get_object_or_404(AdminCharacter, pk=pk)

    if request.method == 'POST':
        form = UserCharacterForm(request.POST)
        if form.is_valid():
            user_character = form.save(commit=False)
            user_character.adminCharacter = admin_character
            user_character.user = request.user
            user_character.save()
            return redirect('character:character_list')
        else:
            print(form.errors)  # 폼 에러 메시지 출력
    else:
        form = UserCharacterForm(initial={'adminCharacter': admin_character})

    return render(request, 'character/character_create_detail.html', {'admin_character': admin_character, 'form': form})

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
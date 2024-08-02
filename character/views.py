from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserCharacter
from django.contrib.auth.models import AnonymousUser  # 로그인 기능없이 테스트를 해보기 위해서
from .forms import UserCharacterNameForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdminCharacter
from .forms import UserCharacterForm


# Create your views here.

def character_list(request):
    if isinstance(request.user, AnonymousUser):
        user_characters = []  # 빈 리스트로 설정하거나 다른 처리를 할 수 있습니다.
    else:
        user_characters = UserCharacter.objects.filter(user=request.user)
    return render(request, 'character/character_list.html', {'user_characters': user_characters})


def character_create(request):
    admin_characters = AdminCharacter.objects.all()
    user_characters = UserCharacter.objects.filter(user=request.user)

    # user2가 가진 모든 AdminCharacter 객체의 ID를 리스트로 추출
    user_character_ids = [uc.adminCharacter.id for uc in user_characters if uc.adminCharacter]

    context = {'admin_characters': admin_characters, 'user_character_ids': user_character_ids}
    return render(request, 'character/character_create.html', context)


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


@login_required
def character_update(request, pk):
    user_character = get_object_or_404(UserCharacter, pk=pk, user=request.user)

    if request.method == 'POST':
        form = UserCharacterNameForm(request.POST, instance=user_character)
        if form.is_valid():
            form.save()
            return redirect('character:character_list')  # 수정 후 캐릭터 리스트로 리다이렉트
    else:
        form = UserCharacterNameForm(instance=user_character)

    return render(request, 'character/character_update.html', {'form': form, 'user_character': user_character})


@login_required
def trash_delete(request, pk):
    if request.method == 'POST':
        UserCharacter.objects.get(pk=pk).delete()
        return redirect('character:trash')
    return render(request, 'user/test.html')


@login_required
def trash(request):
    character_trash = UserCharacter.objects.filter(trash=True)
    context = {'character_trash': character_trash}
    return render(request, 'character/trash.html', context)


@login_required
def trash_restore(request, pk):
    if request.method == 'POST':
        character = UserCharacter.objects.get(pk=pk)
        character.trash = False
        character.save()
        print('gdgdgdgdgd')
    return redirect('character:trash')


@login_required
def trash_perfect_delete(request, pk):
    if request.method == 'POST':
        character = UserCharacter.objects.get(pk=pk)
        character.delete()
    return redirect('character:trash')

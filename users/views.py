from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, User
from django.core.exceptions import ObjectDoesNotExist
import random
# Create your views here.

def main(request):
    user = request.user
    if user.is_anonymous:  # 로그인하지 않은 사용자인 경우 ######
        display_name = "Anonymous User"
    else:
        try:
            profile = Profile.objects.get(user=user)
            display_name = profile.nickname  # 2차 수정
        except ObjectDoesNotExist:
            random_names = ['화사한 유채꽃', '푸른 바다', '밝은 햇살', '고요한 달빛']
            display_name = random.choice(random_names)

    context = {
        'display_name': display_name
    }

    return render(request, 'user/test.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        print("gsdgafsdfasdfasdf")
        # 사용자 존재 여부 확인
        if User.objects.filter(username=username).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용 중인 사용자 이름입니다.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용 중인 이메일 주소입니다.'})
        try:
            user = User.objects.create(
                username=username,
                email=email,
                name=name  # 'name' 필드를 'first_name'으로 사용
            )
            user.set_password(password)  # 비밀번호 해시화
            user.save()

            ################### 프로필 객체 생성 및 닉네임 할당 (2차 수정)
            profile = Profile.objects.create(user=user)
            profile.nickname = profile.get_random_nickname()  # 랜덤 닉네임 할당
            profile.save()

            return redirect('users:login')
        except Exception as e:
            return render(request, 'user/signup.html', {'error': '회원가입에 실패했습니다.'})

    return render(request, 'user/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('character:character_list')
        else:
            return render(request, 'user/signup.html', {'error': '일치하는 계정이 없습니다.'})
    return render(request, 'user/signup.html')


def logout(request):
    auth_logout(request)
    return redirect('users:main')

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        nickname = request.POST.get('nickname', '')
        profile_picture = request.FILES.get('profile_picture')
        delete_picture = request.POST.get('delete_picture') == 'true'

        if nickname == '':
            profile.nickname = ''  # 닉네임 삭제 처리
        else:
            profile.nickname = nickname

        if delete_picture:
            profile.profile_picture = None  # 프로필 사진 삭제 처리
        elif profile_picture:
            profile.profile_picture = profile_picture  # 새 프로필 사진 업로드

        profile.save()
        return redirect('users:profile')

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'user/profile.html', context)

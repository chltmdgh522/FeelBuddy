from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def main(request):
    return render(request, 'user/test.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if username and password and email:
            User = get_user_model()
            user = User.objects.create_user(username=username, password=password, email=email)
            auth_login(request, user)
            return redirect('users:main')
    return render(request, 'user/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('users:main')
        else:
            # 로그인 실패 시
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user/login.html')

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
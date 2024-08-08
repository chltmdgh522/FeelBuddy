from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User


# Create your views here.

def main(request):
    return render(request, 'user/main.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('users:main')  # 로그인된 사용자는 메인 화면으로 리디렉션

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
            return redirect('users:login')
        except Exception as e:
            return render(request, 'user/signup.html', {'error': '회원가입에 실패했습니다.'})

    return render(request, 'user/signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('users:main')  # 로그인된 사용자는 메인 화면으로 리디렉션
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

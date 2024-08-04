from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User


# Create your views here.

def main(request):
    return render(request, 'user/test.html')


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
                password=password,
                name=name  # 'name' 필드를 'first_name'으로 사용
            )
            return redirect('users:login')
        except Exception as e:
            return render(request, 'user/signup.html', {'error': '회원가입에 실패했습니다.'})

    return render(request, 'user/signup.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('users:main')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('users:main')

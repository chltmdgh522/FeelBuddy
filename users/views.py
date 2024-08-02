from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import get_user_model
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
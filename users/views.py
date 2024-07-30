from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

# Create your views here.

def main(request):
    return render(request, 'user/test.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('users:main')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form}) 


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
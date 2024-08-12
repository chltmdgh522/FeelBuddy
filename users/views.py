from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, User
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your views here.

def main(request):
    return render(request, 'user/main.html')

def test(request):
    return render(request, 'user/test.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('users:main')  # 로그인된 사용자는 메인 화면으로 리디렉션

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #name = request.POST.get('name')
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

#비밀번호 재설정 요청
def password_reset_request(request):
    if request.method == 'POST':
        step = request.session.get('password_reset_step', 1)

        if step == 1: #1단계: 사용자 id 확인
            username = request.POST.get('username')
            try:
                user = User.objects.get(username=username)
                request.session['password_reset_username'] = username
                request.session['password_reset_step'] = 2
                return render(request, 'user/password_reset.html', {'step': 2})
            except User.DoesNotExist:
                return render(request, 'user/password_reset.html', {'step': 1, 'error': 'Username not found.'})

        elif step == 2: #2단계: 회원정보에 등록된 이메일 입력
            email = request.POST.get('email')
            username = request.session.get('password_reset_username')
            user = get_object_or_404(User, username=username)

            #입력 받은 이메일이 회원 정보와 일치하는지 확인 후 이메일 전송
            if user.email == email:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                email_subject = 'FeelBuddy: 비밀번호 재설정 메일'
                email_body = render_to_string('user/password_reset_email.txt', {
                    'user': user,
                    'domain': request.get_host(),
                    'uid': uid,
                    'token': token,
                    'protocol': 'http',
                })

                #비밀번호 재설정 이메일 전송
                send_mail(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                request.session['password_reset_step'] = 1
                return redirect('users:password_reset_done')
            else:
                #이메일 일치하지 않을 경우 오류메시지
                return render(request, 'user/password_reset.html', {'step': 2, 'error': 'Email does not match the registered email.'})

    else:
        request.session['password_reset_step'] = 1
        return render(request, 'user/password_reset.html', {'step': 1})

#비밀번호 재설정 요청이 완료된 후 보여줄 페이지
def password_reset_done(request):
    return render(request, 'user/password_reset_done.html')

#비밀번호 재설정 링크를 통해 접근할 뷰
def password_reset_confirm(request, uidb64=None, token=None):
    if uidb64 is None or token is None:
        return redirect('users:password_reset')  # uidb64 또는 token이 없는 경우 처리

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')

            if new_password1 and new_password2 and new_password1 == new_password2:
                user.password = make_password(new_password1)  # 비밀번호 해시화
                user.save()
                return redirect('users:password_reset_complete')
            else:
                return render(request, 'user/password_reset_confirm.html', {
                    'error': 'Passwords do not match.',
                })
    else:
        return render(request, 'user/password_reset_confirm.html', {
            'error': 'Invalid password reset link.',
        })

    return render(request, 'user/password_reset_confirm.html')

#비밀번호 재설정 완료
def password_reset_complete(request):
    return render(request, 'user/password_reset_complete.html')
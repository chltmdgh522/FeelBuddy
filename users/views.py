from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from character.models import UserCharacter
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, User, validate_username, NumViews
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
from django.http import JsonResponse
from django.core.exceptions import ValidationError
#닉네임 랜덤 생성
from django.core.exceptions import ObjectDoesNotExist
import random
# Create your views here.


def main(request):
    user = request.user
    num_views = NumViews.objects.get(id=1)  # 원하는 객체의 ID를 사용하세요.
    num_views.increment()  # 조회수 1 증가

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

    return render(request, 'user/main.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('users:main')  # 로그인된 사용자는 메인 화면으로 리디렉션

    if request.method == 'POST':
        print('gd')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        # 사용자 존재 여부 확인
        if User.objects.filter(username=username).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용 중인 사용자 이름입니다.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용 중인 이메일 주소입니다.'})
        try:
            # 아이디가 영문자와 숫자로 이루어졌는지 확인
            validate_username(username)

            user = User.objects.create(
                username=username,
                email=email,
                name=name,
            )
            user.set_password(password)  # 비밀번호 해시화
            user.save()

            ################### 프로필 객체 생성 및 닉네임 할당 (2차 수정)
            # 이미 존재하는지 확인
            if not Profile.objects.filter(user=user).exists():
                profile = Profile.objects.create(user=user)
                profile.nickname = profile.get_random_nickname()
                profile.save()

            return redirect('users:login')
        except ValidationError as e:
            error_message = " ".join(e.messages)
            return render(request, 'user/signup.html', {'error': f'회원가입에 실패했습니다: {error_message}'})
        except Exception as e:
            return render(request, 'user/signup.html', {'error': f'회원가입에 실패했습니다: {str(e)}'})

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


@login_required
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect('users:main')
    return redirect('users:main')

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        nickname = request.POST.get('nickname', profile.nickname)  # 기존 닉네임 유지
        profile_picture = request.FILES.get('profile_picture')

        profile.nickname = nickname  # 닉네임 업데이트
        if profile_picture:
            profile.profile_picture = profile_picture  # 프로필 사진 업데이트

        profile.save()

        response_data = {
            'nickname': profile.nickname,
            'profile_picture_url': profile.profile_picture.url if profile.profile_picture else ''
        }
        return JsonResponse(response_data)
    first_item = UserCharacter.objects.filter(user=request.user, trash=False).first()
    context = {
        'user': user,
        'profile': profile,
        'first_item':first_item
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
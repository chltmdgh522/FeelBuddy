"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w&ru*a=8k++v5gtnuacib$5(kfes@u!mpzp4@*jclgnv7bu$e&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot',
    'feedback',
    'users',
    'character',


    # 구글 소셜로그인
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 네이버 소셜로그인
    'allauth.socialaccount.providers.naver',
    # 카카오
    'allauth.socialaccount.providers.kakao',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # 구글소셜로그인
]

ROOT_URLCONF = 'config.urls'

AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),  # MySQL 데이터베이스 이름
        'USER': env('DB_USER'),     # MySQL 사용자 이름
        'PASSWORD': env('DB_PASSWORD'),  # MySQL 사용자 비밀번호
        'HOST': env('DB_HOST'),           # MySQL 서버 주소 (로컬 서버의 경우 'localhost' 또는 '127.0.0.1')
        'PORT': '3306',                # MySQL 서버 포트 (기본값은 3306)
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 정적 파일을 찾을 위치를 설정합니다.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 정적 파일이 실제 서빙될 URL 경로를 설정합니다.
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


# 구글 소셜로그인 관련 설정
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'  # 로그인 페이지의 URL 경로
LOGIN_REDIRECT_URL = '/character/list'
#SOCIALACCOUNT_LOGIN_ON_GET = True

# 소셜 계정 프로바이더 설정
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '375689531334-oa582g2gk7dvoo6nn94ggehd5opvcoeb.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'naver': {
        'APP': {
            'client_id': '20M3Zwb2VpH574y0OHQN',
            'secret': 'iDD27qtz9e',
            'key': ''
        }
    },
    'kakao': {
        'APP': {
            'client_id': '4703a49559d7241fea4341b24a9b8dd8',
            'secret': 'FvTb3LFhgpT4jufmI2o3dSwYf33CZE3E',
            'key': ''
        }
    }
}
#비밀번호 재설정 위한 이메일 설정
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jmj00327@gmail.com'
EMAIL_HOST_PASSWORD = 'qzhr lliw epgp chfw'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

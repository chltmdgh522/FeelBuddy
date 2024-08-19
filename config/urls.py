"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import urlpattern
from django.contrib import admin
from django.shortcuts import redirect, render
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


# 404 핸들러
def custom_page_not_found_view(request, exception):
    return redirect('/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('feedback.urls')),
    path('', include('chatbot.urls')),
    path('', include('character.urls')),
    path('accounts/', include('allauth.urls')), #소셜로그인

]

# DEBUG가 False여도 미디어 파일 서빙 가능하게 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 이미지 파일 서빙을 위해 추가
# if not settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404 핸들러 설정
handler404 = 'config.urls.custom_page_not_found_view'
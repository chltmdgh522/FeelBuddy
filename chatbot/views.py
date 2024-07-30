from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from character.models import UserCharacter
from chatbot.models import ChatbotAIContent, ChatbotUserContent


# Create your views here.

@login_required
def chatbot_content_list(request, pk):
    user = request.user
    character = UserCharacter.objects.get(id=pk, user=user)
    ai_contents = ChatbotAIContent.objects.filter(user=user, character=character).order_by('create_ai_time')
    user_contents = ChatbotUserContent.objects.filter(user=user, character=character).order_by('create_user_time')
    context = {
        'ai_contents': ai_contents,
        'user_contents': user_contents,
    }

    return render(request, 'chatbot/chatbotContentList.html', context)


@login_required
def chatbot_ai_create(request, pk):
    if request.method == 'POST':
        user = request.user
        character = UserCharacter.objects.get(id=pk, user=user)
        ChatbotAIContent.objects.create(
            user=user,
            userCharacter=character,
            ai_content=request.POST.get('ai_content'),
        )
        return request.POST.get('ai_content')
    return "get은 없음"


@login_required
def chatbot_user_create(request, pk):
    if request.method == 'POST':
        user = request.user
        character = UserCharacter.objects.get(id=pk, user=user)
        ChatbotUserContent.objects.create(
            user=user,
            userCharacter=character,
            user_content=request.POST.get('user_content'),
        )
        return request.POST.get('user_content')
    return "get은 없음"


@login_required
def emotion(request):
    return 0

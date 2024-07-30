import openai
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from character.models import UserCharacter
from chatbot.models import ChatbotAIContent, ChatbotUserContent

# OpenAI API 키 설정
api_key = "sk-proj-6IG9RLPxkxyEEbH0gcTPT3BlbkFJLB3xdHyQZ0aIDD9XMdqG"
openai.api_key = api_key


@login_required
def chatbot_content_list(request, pk):
    user = request.user
    character = UserCharacter.objects.get(id=pk, user=user)
    ai_contents = ChatbotAIContent.objects.filter(user=user, userCharacter=character).order_by('time')
    user_contents = ChatbotUserContent.objects.filter(user=user, userCharacter=character).order_by('time')

    # 대화 내용을 하나의 리스트로 합치고 시간순으로 정렬
    all_contents = []
    for content in user_contents:
        all_contents.append({
            'type': 'user',
            'content': content.user_content,
            'time': content.time
        })
    for content in ai_contents:
        all_contents.append({
            'type': 'ai',
            'content': content.ai_content,
            'time': content.time
        })

    all_contents.sort(key=lambda x: x['time'])

    context = {
        'all_contents': all_contents,
        'character': character,
    }

    return render(request, 'chatbot/chatbotContentList.html', context)


def ai(system_input, user_input):
    # GPT-4와의 대화
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_input
            },
            {
                "role": "user",
                "content": user_input}
        ],
        max_tokens=1000
    )
    return response.choices[0].message['content']


def character_concept(character):
    system_input = """ """
    if character.adminCharacter.emotion == "분노":
        system_input = """
        너는 분노 캐릭터야 내가 말하는거에 분노에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "슬픔":
        system_input = """
        너는 분노 캐릭터야 내가 말하는거에 분노에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "두려움":
        system_input = """
        너는 분노 캐릭터야 내가 말하는거에 분노에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "불안":
        system_input = """
        너는 분노 캐릭터야 내가 말하는거에 분노에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "좋음":
        system_input = """
        너는 분노 캐릭터야 내가 말하는거에 분노에 공감하면서 답변해줘
        """
    return system_input


@login_required
def chatbot_ai_create(request, pk):
    if request.method == 'POST':
        user = request.user
        character = UserCharacter.objects.get(id=pk, user=user)
        user_input = ChatbotUserContent.objects.filter(
            user=user,
            userCharacter=character
        ).order_by('-time').first()
        print(user_input.user_content)
        system_input = character_concept(character)
        ai_content = ai(system_input, user_input.user_content)
        create = ChatbotAIContent.objects.create(user=user, userCharacter=character, ai_content=ai_content, )

        print("==========================")
        print(ai_content)
        return JsonResponse({'ai_content': ai_content, 'time1': create.time})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def chatbot_user_create(request, pk):
    if request.method == 'POST':
        user = request.user
        character = UserCharacter.objects.get(id=pk, user=user)
        user_content = request.POST.get('user_content')
        create = ChatbotUserContent.objects.create(user=user, userCharacter=character, user_content=user_content, )
        return JsonResponse({'user_content': user_content, 'time1': create.time})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def emotion(request):
    return 0

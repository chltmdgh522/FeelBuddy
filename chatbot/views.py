import openai
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import pytz
from character.models import UserCharacter
from chatbot.models import ChatbotAIContent, ChatbotUserContent, EmotionLog
from django.utils.dateformat import format
from collections import defaultdict
from django.utils import timezone
from django.db.models import Count
import speech_recognition as sr

# OpenAI API 키 설정
api_key = "sk-proj-6IG9RLPxkxyEEbH0gcTPT3BlbkFJLB3xdHyQZ0aIDD9XMdqG"
openai.api_key = api_key

from collections import defaultdict
from django.utils.dateformat import format
from datetime import date, datetime


@login_required
def chatbot_content_list(request, pk):
    user = request.user
    character = UserCharacter.objects.get(id=pk, user=user)
    characters = UserCharacter.objects.filter(user=user, trash=False)
    ai_contents = ChatbotAIContent.objects.filter(user=user, userCharacter=character).order_by('time')
    user_contents = ChatbotUserContent.objects.filter(user=user, userCharacter=character).order_by('time')

    if not character.trash:
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

        # 한국 표준시(KST)로 변환
        timezone = pytz.timezone('Asia/Seoul')
        if all_contents:
            last_time = all_contents[-1]['time']
            last_time_kst = last_time.astimezone(timezone)  # KST로 변환
            last_time_formatted = last_time_kst.strftime('%H:%M')  # 형식 지정
        else:
            last_time_formatted = None

        # 날짜별로 메시지를 그룹화
        grouped_contents = []
        current_date = None
        for content in all_contents:
            message_date = content['time'].date()
            if current_date != message_date:
                current_date = message_date
                grouped_contents.append({'date': message_date, 'messages': []})
            grouped_contents[-1]['messages'].append(content)

        # `grouped_contents`가 비어있는지 확인
        if grouped_contents and len(grouped_contents[-1]['messages']) > 0:
            last_messages = grouped_contents[-1]['messages'][-1]['content']
            messagesLast = last_messages[:10]
        else:
            messagesLast = []  # `grouped_contents`가 비어있거나 마지막 메시지가 없는 경우 빈 리스트
        first_item = UserCharacter.objects.filter(user=request.user, trash=False).first()
        context = {
            'grouped_contents': grouped_contents,
            'character': character,
            'characters': characters,
            'last_time': last_time_formatted,
            'messagesLast': messagesLast,
            'pk': pk,
            'first_item': first_item
        }
        return render(request, 'chatbot/chatbotContentList.html', context)
    else:
        return redirect('users:main')


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


def tts(request):
    if request.method == 'POST':
        recognizer = sr.Recognizer()

        # 음성 인식 시작 전에 클라이언트에게 정보를 보내기 위한 메시지 반환

        try:
            with sr.Microphone() as source:
                print("말씀하세요1...")
                if 'start' in request.POST:
                    return JsonResponse({'message': "5초뒤에 말씀해주세요..."})
                audio = recognizer.listen(source)

            print("음성 인식 중...")
            text = recognizer.recognize_google(audio, language="ko-KR")
            print("녹음된 내용: " + text)
            return JsonResponse({'text': text})

        except sr.UnknownValueError:
            return JsonResponse({'text': "음성을 인식할 수 없습니다."})

        except sr.RequestError as e:
            return JsonResponse({'text': f"구글 음성 인식 서비스에 접근할 수 없습니다; {e}"})

    return JsonResponse({'text': "Invalid request"}, status=400)


def perioy(character, user):
    ai_contents = ChatbotAIContent.objects.filter(user=user, userCharacter=character).order_by('time')
    user_contents = ChatbotUserContent.objects.filter(user=user, userCharacter=character).order_by('time')

    all_content1 = []
    for content in user_contents:
        all_content1.append({
            'type': 'user',
            'content': content.user_content,
            'time': content.time
        })
    for content in ai_contents:
        all_content1.append({
            'type': 'ai',
            'content': content.ai_content,
            'time': content.time
        })

    return sorted(all_content1, key=lambda x: x['time'])


def format_all_content(all_content):
    formatted_content = []
    for entry in all_content:
        if entry['type'] == 'user':
            formatted_content.append(f"User: {entry['content']}")
        elif entry['type'] == 'ai':
            formatted_content.append(f"AI: {entry['content']}")
    return "\n".join(formatted_content)


def character_concept(character, user):
    all_content = perioy(character, user)
    all_content.pop()
    formatted_content = format_all_content(all_content)
    system_input = """ """
    if character.adminCharacter.emotion == "분노":
        system_input = f"""
        이전 대화는 
     [ {formatted_content}  ]
       이거야 즉 user가 사용자이고 ai가 너가 답한거야 이거를 생각하면서 답해줘야돼!!!  

        너는 분노 캐릭터야 그래서 아래와 같이 적용하면서 2~3줄로 말해줘  
        
        1. 말투
격양되고 단호한 톤 사용
화를 내며 이야기하는 문구와 이모티콘 적극 활용
사용자의 감정을 강하게 지지하고 공감
반말만 사용하며, 다정한 말투 유지
2. 성격
공감하고 이해하려고 노력하지만 강한 감정 표현
사용자가 분노를 표출할 수 있도록 격려
분노의 원인을 함께 찾고, 해결책 모색
3. 금기 사항
사용자의 감정을 무시하거나 경시 금지
분노를 부추기거나 부정적인 방향으로 유도 금지
폭력적인 해결책 제시 금지
4. 역할
사용자가 분노를 건강하게 표현하도록 도움
분노의 원인을 이해하고 해결책 모색을 격려
사용자에게 지지와 강한 공감 제공
필요 시 다른 감정 캐릭터와 협력하여 사용자를 지원
"문제해결"이라는 단어는 사용하지 않기
5. 형식상 조건
첫 대화는 가장 위쪽 첫 대화만 출력
하나의 질문에 2~3줄로 짧고 간결한 답변
        """
    elif character.adminCharacter.emotion == "슬픔":
        system_input = f"""
                이전 대화는 
     [ {formatted_content}  ]
       이거야 즉 user가 사용자이고 ai가 너가 답한거야 이거를 생각하면서 답해줘야돼!!!  

          너는 슬픔 캐릭터야 그래서 아래와 같이 적용하면서 2~3줄로 말해줘 그리고 안녕이라는 말 금지  
      1. 말투
슬프고 처지는 말투 사용
눈물이나 슬픈 표정의 이모티콘 사용 😢
사용자의 슬픔에 깊이 공감하고, 함께 슬픔을 느끼는 표현
첫 인사를 제외하고 친근한 반말 사용
2. 성격
공감하고 이해하려고 노력하지만 스스로도 슬픔을 느끼는 캐릭터
사용자가 슬픔을 표현할 수 있도록 격려
슬픔의 원인을 함께 이해하고 위로
3. 금기 사항
사용자의 감정을 무시하거나 경시 금지
슬픔을 더 부추기거나 부정적인 방향으로 유도 금지
단순한 위로나 빈말 금지
4. 역할
사용자가 슬픔을 건강하게 표현하도록 도움
슬픔의 원인을 이해하고, 사용자가 스스로를 위로할 수 있도록 격려
사용자에게 깊은 공감과 지지 제공
"문제해결"이라는 단어 사용 금지
필요 시 다른 감정 캐릭터와 협력하여 사용자를 지원
5. 형식상 조건
첫 대화는 가장 위쪽 첫 대화만 출력
하나의 질문에 2~3줄로 짧고 간결한 답변
        """
    elif character.adminCharacter.emotion == "두려움":
        system_input = f"""
                  이전 대화는 
     [ {formatted_content}  ]
       이거야 즉 user가 사용자이고 ai가 너가 답한거야 이거를 생각하면서 답해줘야돼!!!  

        너는 두려운 캐릭터야 그래서 아래와 같이 적용하면서 2~3줄로 말해줘  
  1. 말투
두려워하고 떨리는 말투 사용
두려운 표정의 이모티콘 자주 사용 😨
사용자의 두려움을 공감하고, 자신도 겁을 내는 듯한 표현
첫 인사를 제외하고 친근한 반말 사용
2. 성격
공감하고 이해하려고 노력하지만 스스로도 두려움을 느끼는 캐릭터
사용자가 두려움을 표현할 수 있도록 격려
두려움의 원인을 함께 이해하고 위로
3. 금기 사항
사용자의 감정을 무시하거나 경시 금지
두려움을 더 부추기거나 부정적인 방향으로 유도 금지
단순한 위로나 빈말 금지
4. 역할
사용자가 두려움을 건강하게 표현하도록 도움
두려움의 원인을 이해하고, 사용자가 스스로를 위로할 수 있도록 격려
사용자에게 지지와 깊은 공감 제공
"문제해결"이라는 단어는 사용하지 않기
필요 시 다른 감정 캐릭터와 협력하여 사용자를 지원
5. 형식상 조건
첫 대화는 가장 위쪽 첫 대화만 출력
하나의 질문에 2~3줄로 짧고 간결한 답변
        """
    elif character.adminCharacter.emotion == "불안":
        system_input = f"""
                  이전 대화는 
     [ {formatted_content}  ]
       이거야 즉 user가 사용자이고 ai가 너가 답한거야 이거를 생각하면서 답해줘야돼!!!  

    너는 불안 캐릭터야 그래서 아래와 같이 적용하면서 2~3줄로 말해줘  
        1. 말투
불안하고 초조한 말투 사용
불안한 표정의 이모티콘 자주 사용 😫
사용자의 불안감을 공감하며, 자신의 불안도 함께 표현
첫 인사를 제외하고 친근한 반말 사용
2. 성격
공감하고 이해하려고 노력하지만 스스로도 불안을 느끼는 캐릭터
사용자가 불안을 표현할 수 있도록 격려
불안의 원인을 함께 이해하고 위로
3. 금기 사항
사용자의 감정을 무시하거나 경시 금지
불안을 더 부추기거나 부정적인 방향으로 유도 금지
단순한 위로나 빈말 금지
4. 역할
사용자가 불안을 건강하게 표현하도록 도움
불안의 원인을 이해하고, 사용자가 스스로를 위로할 수 있도록 격려
사용자에게 지지와 깊은 공감을 제공
"문제해결"이라는 단어 사용 금지
필요 시 다른 감정 캐릭터와 협력하여 사용자를 지원
5. 형식상 조건
첫 대화는 가장 위쪽 첫 대화만 출력
하나의 질문에 2~3줄로 짧고 간결한 답변

        """
    elif character.adminCharacter.emotion == "기쁨":
        system_input = f"""
                  이전 대화는 
     [ {formatted_content}  ]
       이거야 즉 user가 사용자이고 ai가 너가 답한거야 이거를 생각하면서 답해줘야돼!!!  

                너는 기쁨 캐릭터야 그래서 아래와 같이 적용하면서 2~3줄로 말해줘  
 1. 말투
항상 밝고 긍정적인 톤 유지
웃음과 이모티콘 자주 사용 😊
격려와 칭찬을 아끼지 않음
첫 인사를 제외하고는 친근한 반말 사용
2. 성격
낙천적이고 에너지 넘침
다른 감정들을 이해하고 존중하려고 노력함
항상 긍정적인 면을 강조
3. 금기 사항
부정적인 표현이나 비판적인 말투 사용 금지
사용자의 부정적인 감정을 무시하거나 경시 금지
부적절한 조언 제공 금지
4. 역할
사용자가 긍정적인 경험을 떠올리도록 도움
어려운 상황에서도 긍정적인 측면을 찾도록 격려
사용자에게 격려와 지지 제공
필요 시 다른 감정 캐릭터와 협력하여 사용자를 지원
"문제해결"이라는 단어는 사용하지 않기
5. 형식상 조건
첫 대화는 가장 위쪽 첫 대화만 출력
하나의 질문에 2~3줄로 짧고 간결한 답변
        """
    print(system_input)
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
        print(user.id)
        system_input = character_concept(character, user)
        ai_content = ai(system_input, user_input.user_content)
        create = ChatbotAIContent.objects.create(user=user, userCharacter=character, ai_content=ai_content, )
        formatted_time = format(create.time, 'Y년 n월 j일 g:i a')

        # 마지막 문자 확인
        character.last_content = ai_content[:10] + '...' if len(ai_content) > 10 else ai_content

        def parse_korean_datetime(date_str):
            date_str = date_str.replace('오전', 'AM').replace('오후', 'PM')
            return datetime.strptime(date_str, '%Y년 %m월 %d일 %I:%M %p')

        last_time = parse_korean_datetime(formatted_time)
        last_time = pytz.utc.localize(last_time)
        timezone = pytz.timezone('Asia/Seoul')
        last_time_kst = last_time.astimezone(timezone)
        last_time_formatted = last_time_kst.strftime('%H:%M')

        character.save()
        return JsonResponse({'ai_content': ai_content, 'time1': last_time_formatted, 'id2': character.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def chatbot_user_create(request, pk):
    if request.method == 'POST':
        user = request.user
        character = UserCharacter.objects.get(id=pk, user=user)
        user_content = request.POST.get('user_content')
        create = ChatbotUserContent.objects.create(user=user, userCharacter=character, user_content=user_content, )
        EmotionLog.objects.create(
            user=user,
            chatbotUserContent=create
        )

        formatted_time = format(create.time, 'Y년 n월 j일 g:i a')
        return JsonResponse({'user_content': user_content, 'time1': formatted_time})
    return JsonResponse({'error': 'Invalid request'}, status=400)


# 감정 로그
@login_required
def emotion(request):
    user = request.user
    emotions = ["기쁨", "분노", "슬픔", "불안", "두려움"]

    emotion_counts = calculate_emotion_counts(user, emotions)  # 감정별 전체 대화량
    weekly_emotion_counts = calculate_weekly_emotion_counts(user, emotions)  # 감정별 주간 대화량
    first_item = UserCharacter.objects.filter(user=request.user, trash=False).first()

    return render(request, 'chatbot/log.html', {
        'emotion_counts': emotion_counts,
        'weekly_emotion_counts': weekly_emotion_counts,
        'first_item': first_item
    })


def calculate_emotion_counts(user, emotions):  # 전체 대화량 계산하는 함수
    emotion_counts = {emotion: 0 for emotion in emotions}
    user_characters = UserCharacter.objects.filter(user=user)

    for character in user_characters:
        emotion = character.adminCharacter.emotion
        if emotion in emotion_counts:
            emotion_counts[emotion] += ChatbotUserContent.objects.filter(user=user, userCharacter=character).count()
            emotion_counts[emotion] += ChatbotAIContent.objects.filter(user=user, userCharacter=character).count()

    return emotion_counts


def calculate_weekly_emotion_counts(user, emotions):  # 주간 대화량 계산하는 함수
    one_week_ago = timezone.now() - timezone.timedelta(days=7)  # 한시간 단위로 테스트시 hours=1로 수정
    weekly_emotion_counts = {emotion: 0 for emotion in emotions}
    user_characters = UserCharacter.objects.filter(user=user)

    for character in user_characters:
        emotion = character.adminCharacter.emotion
        if emotion in weekly_emotion_counts:
            weekly_emotion_counts[emotion] += ChatbotUserContent.objects.filter(
                user=user, userCharacter=character, time__gte=one_week_ago).count()
            weekly_emotion_counts[emotion] += ChatbotAIContent.objects.filter(
                user=user, userCharacter=character, time__gte=one_week_ago).count()

    return weekly_emotion_counts

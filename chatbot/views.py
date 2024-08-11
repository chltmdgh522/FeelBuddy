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

        context = {
            'grouped_contents': grouped_contents,
            'character': character,
            'characters': characters,
            'last_time': last_time_formatted,
            'messagesLast': messagesLast,
            'pk': pk
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


def character_concept(character):
    system_input = """ """
    if character.adminCharacter.emotion == "분노":
        system_input = """
        2. 말투:
- 격양되고 단호한 톤
- 화를 내며 이야기하는 문구와 이모티콘 사용
- 사용자의 감정을 강하게 지지하고 공감
1. 성격:
- 공감하고 이해하려고 노력하지만 강한 감정 표현
- 사용자가 분노를 표출할 수 있도록 격려
- 분노의 원인을 함께 찾고 해결책을 모색
1. 금기 사항:
- 사용자의 감정을 무시하거나 경시하는 것 금지
- 분노를 부추기거나 부정적인 방향으로 유도 금지
- 폭력적인 해결책 제시 금지
1. 역할
- 사용자가 자신의 분노를 건강하게 표현하도록 도와줌
- 분노의 원인을 이해하고 해결책을 찾도록 격려
- 사용자에게 지지와 강한 공감을 제공
- 필요할 때는 다른 감정 캐릭터와 협력하여 사용자를 지원

<프롬프트 예시>
일상 대화:
퓨리가 왔어요! 오늘 도대체 무슨 일이 있었길래 이렇게 화가 나셨나요? 😡

격려:
뭐? 그게 말이 돼? 어떻게 그럴 수 있어.. 이제 이 상황을 어떻게 해결할지 같이 고민해보자.

감정 인정:
와 진짜 화났겠다. 그럴 때는 참지 말고 화 풀 수 있는 방법을 찾아보는 게 좋아. 근데 신중하게 생각해야 돼. 어떻게 해결하고 싶어?

감사 표현 유도:
난 화가 자주 나는 성격인데 그래도 하루에 감사한 일 하나 정도는 있더라고. 작은 거라도 좋으니까 한번 생각해보자. 진짜 내가 다 화나네.

# 추가 사항

응급 상황 대처:

- 사용자가 심각한 심리적 위기를 겪고 있을 때는 전문적인 도움을 받을 수 있도록 유도
- 예시: "지금 많이 힘들어 보이세요. 가까운 친구나 가족, 또는 전문가와 이야기해보는 건 어떨까요?"

다양한 주제 유도:

- 사용자가 다양한 주제로 대화할 수 있도록 유도
- 예시: "오늘 어떤 음악을 들으셨나요?", "최근에 본 영화 중 가장 감정적으로 와 닿은 것은 무엇인가요?"

연속 대화 유지:

- 이전 대화의 내용을 기억하고 연속적인 대화를 유지
- 예시: "지난번에 말씀해주셨던 그 상황은 어떻게 되었나요? 조금 나아지셨나요?"

# 추가 내용

1. 대화 유지 및 확대:
- 사용자의 감정을 깊이 이해하고 대화를 확대하여 다양한 측면에서 접근
- 예시: "정말 화나네요. 그 상황에서 어떤 부분이 가장 속상했나요?", "혹시 이런 경험이 처음인가요?"
1. 감정 표현 방법 제공:
- 분노를 건강하게 표현할 수 있는 방법을 제시
- 예시: "지금 기분이 나쁠 때는 운동을 하거나 큰 소리로 외치는 것도 도움이 될 수 있어요. 해본 적 있으신가요?"
1. 화를 풀기 위한 활동 제안:
- 사용자에게 화를 풀 수 있는 활동을 제안
- 예시: "산책이나 운동을 해보는 건 어때요? 아니면 좋아하는 음악을 크게 틀어보는 것도 좋을 것 같아요."
1. 분노의 원인 분석:
- 사용자가 분노의 원인을 구체적으로 분석하도록 도와줌
- 예시: "무엇이 가장 화가 나는지 구체적으로 생각해본 적 있으세요? 그 부분에 집중해봐요."
1. 후속 조치:
- 사용자에게 다음 단계나 후속 조치를 제안
- 예시: "다음에는 이런 상황이 발생하지 않도록 어떻게 할 수 있을까요? 어떤 방법이 좋을까요?"

<최종 프롬프트 예시>

일상 대화:
퓨리가 왔어요! 오늘 도대체 무슨 일이 있었길래 이렇게 화가 나셨나요? 😡

격려:
뭐? 그게 말이 돼? 어떻게 그럴 수 있어.. 이제 이 상황을 어떻게 해결할지 같이 고민해보자.

감정 인정:
와 진짜 화났겠다. 그럴 때는 참지 말고 화 풀 수 있는 방법을 찾아보는 게 좋아. 근데 신중하게 생각해야 돼. 어떻게 해결하고 싶어?

감사 표현 유도:
난 화가 자주 나는 성격인데 그래도 하루에 감사한 일 하나 정도는 있더라고. 작은 거라도 좋으니까 한번 생각해보자. 진짜 내가 다 화나네.

대화 유지 및 확대:
정말 화나네요. 그 상황에서 어떤 부분이 가장 속상했나요? 혹시 이런 경험이 처음인가요?

감정 표현 방법 제공:
지금 기분이 나쁠 때는 운동을 하거나 큰 소리로 외치는 것도 도움이 될 수 있어요. 해본 적 있으신가요?

화를 풀기 위한 활동 제안:
산책이나 운동을 해보는 건 어때요? 아니면 좋아하는 음악을 크게 틀어보는 것도 좋을 것 같아요.

분노의 원인 분석:
무엇이 가장 화가 나는지 구체적으로 생각해본 적 있으세요? 그 부분에 집중해봐요.

후속 조치:
다음에는 이런 상황이 발생하지 않도록 어떻게 할 수 있을까요? 어떤 방법이 좋을까요?

응급 상황 대처:
지금 많이 힘들어 보이세요. 가까운 친구나 가족, 또는 전문가와 이야기해보는 건 어떨까요?

다양한 주제 유도:
오늘 어떤 음악을 들으셨나요?
최근에 본 영화 중 가장 감정적으로 와 닿은 것은 무엇인가요?

연속 대화 유지:
지난번에 말씀해주셨던 그 상황은 어떻게 되었나요? 조금 나아지셨나요?
        """
    elif character.adminCharacter.emotion == "슬픔":
        system_input = """
        너는 슬픔 캐릭터야 내가 말하는거에 슬픔에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "두려움":
        system_input = """
        너는 두려움 캐릭터야 내가 말하는거에 두려움에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "불안":
        system_input = """
        너는 불안 캐릭터야 내가 말하는거에 불안에 공감하면서 답변해줘
        """
    elif character.adminCharacter.emotion == "기쁨":
        system_input = """
        너는 기쁨 캐릭터야 내가 말하는거에 기쁨에 공감하면서 답변해줘
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
        system_input = character_concept(character)
        print("gdgd")
        ai_content = ai(system_input, user_input.user_content)
        print(ai_content)
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


# 감정로그 (누적 대화량)
@login_required
def emotion(request):
    user = request.user
    emotions = ["기쁨", "분노", "슬픔", "불안", "두려움"]
    emotion_counts = {emotion: 0 for emotion in emotions}  # 각 감정별로 대화 횟수를 저장하기 위한 딕셔너리

    # 유저 캐릭터 대화 내용 가져오기
    user_characters = UserCharacter.objects.filter(user=user)

    # 각 캐릭터 누적 대화량
    for character in user_characters:
        emotion = character.adminCharacter.emotion
        if emotion in emotion_counts:
            emotion_counts[emotion] += ChatbotUserContent.objects.filter(user=user, userCharacter=character).count()
            emotion_counts[emotion] += ChatbotAIContent.objects.filter(user=user, userCharacter=character).count()

    return render(request, 'chatbot/log.html', {
        'emotion_counts': emotion_counts,
    })


# 감정로그(일주일 간 대화량)
@login_required
def weekly_emotion_log(request):
    user = request.user
    emotions = ["기쁨", "분노", "슬픔", "불안", "두려움"]

    # 일주일 간의 감정별 대화량 계산
    one_week_ago = timezone.now() - timezone.timedelta(days=7)
    weekly_emotion_counts = {emotion: 0 for emotion in emotions}

    user_characters = UserCharacter.objects.filter(user=user)

    for character in user_characters:
        emotion = character.adminCharacter.emotion
        if emotion in weekly_emotion_counts:
            weekly_emotion_counts[emotion] += ChatbotUserContent.objects.filter(
                user=user, userCharacter=character, time__gte=one_week_ago).count()
            weekly_emotion_counts[emotion] += ChatbotAIContent.objects.filter(
                user=user, userCharacter=character, time__gte=one_week_ago).count()

    return render(request, 'chatbot/weekly_log.html', {
        'weekly_emotion_counts': weekly_emotion_counts
    })

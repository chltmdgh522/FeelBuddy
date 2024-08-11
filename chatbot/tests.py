import speech_recognition as sr

# 음성 인식 객체 생성
recognizer = sr.Recognizer()

# 마이크로부터 입력 받기
with sr.Microphone() as source:
    print("말씀하세요 (5초 제한)...")
    audio = recognizer.listen(source, phrase_time_limit=5)  # 최대 5초 동안 녹음


# 음성을 텍스트로 변환
try:
    print("음성 인식 중...")
    text = recognizer.recognize_google(audio, language="ko-KR")
    print("녹음된 내용: " + text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print(f"구글 음성 인식 서비스에 접근할 수 없습니다; {e}")
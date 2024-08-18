![image](https://github.com/user-attachments/assets/01064bcd-76ba-4491-9c51-70f84f4b2a5b)

# 📰 FEELBUDDY
##### 🏆 피로그래밍 21기 최종 프로젝트 작품

### 📜 Contents
 1. [Overview](#-overview)
 2. [서비스 화면](#-서비스-화면)
 3. [주요 기능](#-주요-기능)
 4. [개발 환경](#%EF%B8%8F-개발-환경)
 5. [시스템 아키텍처](#-시스템-아키텍처)
 6. [기술 특이점](#-기술-특이점)
 7. [기획 및 설계 산출물](#-기획-및-설계-산출물)
 8. [Conventions](#-conventions)
 9. [팀원 소개](#-팀원-소개)
 
## ✨ Overview

> 각각의 개성을 가진 캐릭터들과 대화하여 감정을 치유하는 웹 서비스

## ✨ FEELBUDDY의 배포 사이트
##### 🏆 [사이트](https://feelbuddy.kr/)



## ✨ FEELBUDDY의 소통 플랫폼 
##### 🏆 [노션](https://www.notion.so/Feelbuddy-6330c0b568714b6ab0a4659d635ad782)
##### 🏆 [ZEP](https://zep.us/)


## 👀 서비스 화면
### ✨ 모든 페이지 `모바일(아이폰 12 Pro 기준 max-width:480px)` 지원


### 홈
- 닌텐도 화면 적용
- 화면이 작아질 수록 DS - GBA - GDC 로 구현했다.
- Start 버튼을 통해 캐릭터리스트로 갈 수 있다.
- 로그인 및 회원가입 버튼을 누르수 있다
  
<div>
  <img src="https://github.com/user-attachments/assets/ece63fc2-ca98-441d-9a4c-ddc80e4b7c6b" width="75%"/>
  <img src="https://github.com/user-attachments/assets/ff5d977d-9281-4e4a-b1ce-020682c30086" width="20%"/>
</div>


### 회원가입 & 로그인 & 로그아웃
- `네이버, 카카오 구글 소셜 로그인` 및 유저 회원가입/로그인
- 로그인을 하면 캐릭터 리스트로 넘어간다.
<div>
<img src="https://github.com/user-attachments/assets/0e57d0ce-0ad5-4dac-9ff1-0c662a67d439" width="20%"/>
<img src="https://github.com/user-attachments/assets/b97d5b9e-feef-414d-9360-d90527ecb66f" width="75%">
</div>


### 마이페이지
- `프로필 이미지 변경`
- `닉넴임 변경`
<div>
<img src="https://github.com/user-attachments/assets/34053b7f-a080-4a15-9e72-bcdf90e28dd0" width="75%">
<img src="https://github.com/user-attachments/assets/5e5e1139-14d8-4a05-86ca-0d2a9ad82018" width="20%">
</div>


### 캐릭터 리스트
- 생성, 삭제, 편집 버튼을 이용해 캐릭터 관리 
<div>
<img src="https://github.com/user-attachments/assets/b153ded0-f9ce-4879-a4b9-a610c65515ce" width="20%">
<img src="https://github.com/user-attachments/assets/9a6c0d05-4b62-4656-bb69-3878b0e4e9e7" width="75%">
</div>



### 캐릭터 생성
- 5개의 캐릭터 중 하나를 뽑는다. 하지만 이미 생성된 캐릭터는 못 고른다.
- 캐릭터의 이름과 선택한 이유를 적으면 생성이 된다.
<div>
<img src="https://github.com/user-attachments/assets/30e88da7-8b5b-40be-b4dc-1df85bc1b333" width="75%">
<img src="https://github.com/user-attachments/assets/80557388-2081-4a7a-8b18-91fce71355fa" width="20%">
</div>


### 휴지통
- 캐릭터 리스트에서 버린 캐릭터들을 볼 수 있다.
- 여기서는 복구 및 영구 삭제를 할 수 있다. 
<div>
<img src="https://user-images.githubusercontent.com/33210124/193836104-9f9af9af-48df-490d-99a7-2066b999c47d.gif" width="20%">
<img src="https://github.com/user-attachments/assets/2c5642fe-11b9-421d-8891-6d827256086f" width="75%">
</div>

  
### 챗봇 
- 음성 인식을 통해 대화를 할 수 있다.
- 영상통화 버전에서는 TTS 구현되어있다.
- Ajax를 통해 실시간으로 캐릭터와 채팅! 
<div>
<img src="https://github.com/user-attachments/assets/3d1a2ca3-fcb7-49c9-b991-172636f5c0c2" width="75%"/>
<img src="https://github.com/user-attachments/assets/2afcf85a-804e-4647-819b-3a02022202e8" width="20%"/>
</div>

<div>
<img src="https://github.com/user-attachments/assets/2afcf85a-804e-4647-819b-3a02022202e8" width="20%"/>
<img src="https://github.com/user-attachments/assets/76c34384-8782-4794-b18c-1a31cd966f6f" width="75%"/>
</div>




### 피드백
- 별점 및 리뷰를 통해 해당 에플리케이션의 평가를 알 수 있다.
- 피드백을 통해 추후 계속 업데이트 할 예정이다.
 <div>
<img src="https://github.com/user-attachments/assets/27097924-b693-4c12-aca7-93dc3a93b3c2" width="75%">
<img src="https://github.com/user-attachments/assets/444327ce-8070-4f2b-9b6d-242c0661db92" width="20%">
</div>



### 감정 로그
- 5개의 캐릭터들과 챗봇을 통해 나온 결과를 보여준다.
- 주간 및 누적 기능이 있어 감저의 정보를 쉽게 파악할 수 있다.
<div>
<img src="https://github.com/user-attachments/assets/9aa369fc-a257-4693-a5ce-6772540210e2" width="20%">
<img src="https://github.com/user-attachments/assets/44cad03c-362b-4fc8-a86a-7e844ceb8c20" width="75%">
</div>

  
## ✨ 주요 기능

- `캐릭터 기능`
	- 분노, 기쁨, 불안, 두려움, 불안 총 5개의 캐릭터를 생성할 수 있다. 
  - 생성된 캐릭터를 수정 및 휴지통에 버릴 수 있다. 
	- 휴지통에 버려진 캐릭터는 다시 복구 할 수 있고 영원히 삭제할 수 있다.
	
- `프롬프트 설계`
	- 총 5개의 캐릭터마다 프롬프트를 설계한다. 
	- 프롬프트에 이전 대화를 기억할 수 있도록 DB에서 해당 데이터를 찾아와 프롬프트에 넘겨준다.
  
- `실시간 AI와 챗봇`
	- Open AI를 통해 API와 연결한뒤 사용자 답변에 따른 AI 답변이 제공이 된다.
	- Ajax를 통해 실시간으로 대화가 진행되며 시간 마지막 답변들도 실시간으로 추가가 된다. 
   
- `챗봇 TTS`
	- 영상 통화 화면에 넘어간뒤 사용자가 답하면 AI 답변이 TTS로 제공이 된다. 
	- 여러 목소리 TTS 기능이 설정이 되어있다.

- `감정 로그`
	- 사용자가 각각의 캐릭터마다 대화한 기록을 수치화하여 로그로 보여준다. 
	- 누적 및 주간이 있어 해당 감정 로그를 확인할 수 있다.

- `피드백`
	- 사용자들이 서비스를 이용하고 나서 후기를 올리 수 있는 공간이다.
   
- `회원 관리`
	- 네이버, 구글, 카카오 소셜 로그인 기능을 도입했다. 
	- 비밀번호 재설정 기능 도입했다.  
   
- `사용자 친화적 UI`
	- 반응형 모바일 뷰 지원
	- 색다른 3D CSS 도입

## 🖥️ 개발 환경

**Management Tool**
- 형상 관리 : Git
- 이슈 관리 : Jira
- 커뮤니케이션 : Zep, Notion
- 디자인 : Figma

**🐳 Backend**
- Python `3.8.0`
- Django `4.2.x`
- Django Rest Framework `3.12.x`
- pipenv or poetry (패키지 관리 도구)
- MySQL  `8.0.4`
- Gunicorn `20.1.0` (배포용 WSGI 서버)
- Swagger (`drf-yasg`)
- Django Rest Framework SimpleJWT (JWT 인증)
- Celery `5.x.x` (비동기 작업 처리)
- Redis `6.x.x` (캐시 및 Celery 브로커)
- Jupyter Notebook `6.4.12`
- Apache Spark `3.2.1`


**🦊 Frontend**
- lang: HTML5, CSS3, JAVASCRIPT

**🖼️ Requirements.txt**
```plaintext
aiohttp==3.9.5
aiosignal==1.3.1
annotated-types==0.7.0
anyio==4.4.0
asgiref==3.8.1
attrs==23.2.0
certifi==2024.7.4
cffi==1.16.0
charset-normalizer==3.3.2
colorama==0.4.6
contourpy==1.2.1
cryptography==43.0.0
cycler==0.12.1
distro==1.9.0
Django==5.0.8
django-allauth==0.63.6
django-environ==0.11.2
fonttools==4.53.1
frozenlist==1.4.1
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
idna==3.7
jwt==1.3.1
kiwisolver==1.4.5
matplotlib==3.9.0
multidict==6.0.5
mysqlclient==2.2.4
numpy==2.0.1
openai==0.28.0
packaging==24.1
pillow==10.4.0
PyAudio==0.2.14
pycparser==2.22
pydantic==2.8.2
pydantic_core==2.20.1
pydub==0.25.1
PyJWT==2.8.0
PyMySQL==1.1.1
pyparsing==3.1.2
python-dateutil==2.9.0.post0
pytz==2024.1
requests==2.32.3
setuptools==72.1.0
six==1.16.0
sniffio==1.3.1
SpeechRecognition==3.10.4
sqlparse==0.5.1
tqdm==4.66.4
typing_extensions==4.12.2
tzdata==2024.1
urllib3==2.2.2
yarl==1.9.4
```

**🗝️ API**
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)   
- [OpenAI](https://openai.com/)

**🗂️ DB**
- MySQL `8.0.30`

**🌐 Server**
- AWS EC2 (Ubuntu `20.04`)
- Nginx `1.23` (Reverse Proxy)
- Gunicorn `20.1.0` (WSGI Application Server)
- HTTPS (TLS `1.2`)

**🔨 IDE**
- Pycharm `2023.2`
- MySQL Workbench `8.0.29`
- VSCode `1.69.2`

## 💫 시스템 아키텍처

![image](https://github.com/user-attachments/assets/265a7eca-8434-411e-841d-2d1887dabc82)


## ✨ 기술 특이점

- **캐릭터별 고유 프롬프트**를 사용하여 사용자 경험을 맞춤화
- 사용자가 선택한 캐릭터에 따라 다른 프롬프트가 적용되어 대화 진행
- 각 캐릭터는 고유한 성격과 대화 스타일을 가지고 있으며, 감정 분석 결과에 따라 다양한 반응을 생성
- OpenAI의 GPT 모델을 활용하여 실시간 감정 분석 및 캐릭터 기반 응답 제공
- Celery를 통해 대규모 사용자 요청을 효율적으로 비동기 처리하여 서버 성능 최적화


# 📂 기획 및 설계 산출물

### [💭 요구사항 정의 및 기능 명세](https://www.notion.so/Feelbuddy-6330c0b568714b6ab0a4659d635ad782)

![image](https://github.com/user-attachments/assets/608d90da-08f0-4e0e-bffe-09c32e2be53f)


### [🎨 화면 설계서](https://www.figma.com/design/2MIHENt866R7jjAyDBO3lp/Untitled?node-id=0-1)

![image](https://github.com/user-attachments/assets/ce15a380-b42c-49c6-906a-d86d37250992)


### [✨ ER Diagram](https://www.erdcloud.com/d/p9ocstx53DrdNzupt)

![image](https://github.com/user-attachments/assets/135eac39-5e08-42a9-b97f-6bf5afe6fdf4)


# 💞 팀원 소개
##### ❤️‍🔥 FEELBUDDY를 개발한 `피로그래밍 21기` 팀원들을 소개합니다!

| **[나예원](https://github.com/Anna-user)** | **[최승호](https://github.com/chltmdgh522)** | **[전진명](https://github.com/JNMYNG)** | **[이민수](https://github.com/msoolee)** |
| :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://github.com/user-attachments/assets/77267564-6b13-4213-a28f-67acf7840f48" width="400"> | <img src="https://github.com/user-attachments/assets/e792dfc6-e2a7-4b42-b5a5-27672d4df6c7" width="400"> | <img src="https://github.com/user-attachments/assets/aec44d20-60ee-4411-9a6f-8dba81ff5403" width="400"> | <img src="https://github.com/user-attachments/assets/9e92ceed-574a-4bbb-80ff-78ea2587f4c2" width="400"> |
| Leader & Frontend & Designer | Backend & AI | Backend | Frontend & Backend |



## 😃 팀원 역할

- **나예원**
  - 팀장, 디자인, 프론트, 와이어프레임 설계, 3D CSS 설계
- **최승호**
  - ERD 설계, 챗봇 기능, 캐릭터 관리 기능, REST API 설계, AWS 서버 배포
- **전진명**
  - 회원관리, 마이페이지, 피드백, 감정 로그 
- **이민수**
  - 감성 글귀, User 닉네임 랜덤 기능, 캐릭터 생성관리 기능, 인스타 광고, flutter webview 

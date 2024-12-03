[![CD Pipeline](https://github.com/chltmdgh522/FeelBuddy/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/chltmdgh522/FeelBuddy/actions/workflows/deploy.yml)
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
##### 🏆 개발 기간: 24.07.01 ~ 24.08.20
> 
현대 사회에서 많은 사람들이 스트레스와 우울감을 경험하고 있으며, 이를 해결하기 위한 심리적 지원이 필요합니다. 하지만 정신 건강 전문가와의 상담은 비용과 시간이 많이 들고, 접근성의 문제도 있을 수 있습니다. 실시간 감정 치유 웹 서비스는 이러한 문제를 해결하기 위한 대안으로, 사용자가 각기 다른 개성을 가진 캐릭터들과 대화를 통해 감정적 지지를 받을 수 있게 합니다. 특히, 현대인들이 쉽게 접근할 수 있는 디지털 플랫폼을 통해, 언제 어디서나 감정 상태를 공유하고 위로를 받을 수 있다는 점에서 유용합니다.

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
<img src="https://github.com/user-attachments/assets/2f525651-67e9-42da-95f6-448dc40eba47" width="20%">
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
<img src="https://github.com/user-attachments/assets/e8f38e20-c9c6-40e6-847e-9f00ebbedbd8" width="20%"/>
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
   
- `중요도 지표`
	- 사용자 대화가 들어오면 중요도 지표를 계산한뒤 중요한 대화를 선별해서 50건만 저장되도록 설계했다. 
	- 중요 대화 50건이 만약 채웠을경우 덜 중요한 대화 기록을 뺴고 새로 저장한다.
   
- `챗봇 TTS`
	- 영상 통화 화면에 넘어간뒤 사용자가 답하면 AI 답변이 TTS로 제공이 된다. 
	- 여러 목소리 TTS 기능이 설정이 되어있다.

- `감정록
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
| <img src="https://github.com/user-attachments/assets/7f6428b7-e110-40ed-98b1-be6e595c9f79" width="400"> | <img src="https://github.com/user-attachments/assets/e792dfc6-e2a7-4b42-b5a5-27672d4df6c7" width="400"> | <img src="https://github.com/user-attachments/assets/aec44d20-60ee-4411-9a6f-8dba81ff5403" width="400"> | <img src="https://github.com/user-attachments/assets/9e92ceed-574a-4bbb-80ff-78ea2587f4c2" width="400"> |
| Leader & Frontend & Designer | Backend & AI | Frontend & Backend |  Backend |




## 😃 팀원 역할

- **나예원**
  - 팀장, 기획, 캐릭터 및 로고 디자인, 프론트, 와이어프레임 설계, 3D CSS 설계, AI 프롬프트 설계
- **최승호**
  - ERD 설계, 챗봇 기능, 캐릭터 관리 기능, REST API 설계, AWS 서버 배포 및 CICD 설정
- **전진명**
  - 회원관리, 마이페이지, 피드백, 감정 로그 
- **이민수**
  - 감성 글귀, User 닉네임 랜덤 기능, 캐릭터 생성관리 기능, 인스타 광고, flutter webview 

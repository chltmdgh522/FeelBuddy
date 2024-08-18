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



## ✨ FEELBUDDY의 플랫폼 
##### 🏆 [노션]([https://feelbuddy.kr/](https://www.notion.so/Feelbuddy-6330c0b568714b6ab0a4659d635ad782))


## 👀 서비스 화면
### ✨ 모든 페이지 `다크모드`, `모바일(아이폰 12 Pro 기준 max-width:480px)` 지원

### 온보딩
- `fullpage`를 적용한 온보딩
- 지구본 상호작용
- 모바일 버전에서는 클릭을 통한 fullpage 동작
<div width="100%">
<img src="https://user-images.githubusercontent.com/33210124/193836094-3963aa71-8c62-438c-8de7-1ace6a4c6db9.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/193836099-d01808f4-f0f5-4f80-87d3-c78a5e8a5af3.gif" width="20%">
</div>

### 회원가입 & 로그인 & 로그아웃
- `구글 메일 인증`을 통한 유저 회원가입/로그인
<div>
<img src="https://user-images.githubusercontent.com/33210124/193836111-c600761d-abc2-4007-a4b8-309e97a6ab7a.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/193836125-0ec0632b-ccd0-4d4c-b8e2-05cd1b7081a9.gif" width="20%">
</div>
  
### 마이페이지
- `프로필 이미지 변경`
- 내가 `스크랩한 기사, 나만의 단어장, 내가 획득한 뱃지, 내 관심 카테고리` 표현
<div>
<img src="https://user-images.githubusercontent.com/33210124/195591883-974fd700-addd-4a32-8e80-ae4da2d5f99d.gif" width="20%">
<img src="https://user-images.githubusercontent.com/33210124/195591865-c16d131c-3ada-4bd9-8221-69b4e520de00.gif" width="75%">
</div>

### 배지 획득
- `출석`, `레벨`, `게임`, `단어장 추가`, `기사 스크랩` 에 대한 배지 부여
<div>
<img src="https://user-images.githubusercontent.com/33210124/194193047-55ceea30-b72c-4e22-aee6-829dca7060ce.png" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/194193041-89da59da-2417-470a-a997-c0362d14f9da.png" width="20%">
</div>
<div>
<img src="https://user-images.githubusercontent.com/33210124/194193045-9d9d4204-a72a-4e6d-aa95-105c397f4f91.png" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/194193046-157f5d78-8d46-47c3-9e81-1d075398fbc7.png" width="20%">
</div>

### 랜딩 (HOME)
- 사용자의 카테고리, 레벨에 따른 `사용자 추천(USER FIT) 기사` 제공
- 하루 중 `가장 많은 조회수를 기록한 기사(HOT TOPIC)` 제공
- 하루의 뉴스 기사에서 추출한 `데일리 워드 클라우드` 제공
    - 해당 워드 클라우드 기사들 함께 제공
<div>
<img src="https://user-images.githubusercontent.com/33210124/194319730-d5212912-ff4f-4179-b419-8c066c5b2e57.gif" width="20%">
<img src="https://user-images.githubusercontent.com/33210124/194319846-63bc5e01-8fe1-417b-8ab1-4432703c659d.gif" width="75%">
</div>

### 레벨 테스트
- 6단계의 영단어 제시를 통해 나만의 영어 레벨 확인하기
- `유럽연합 공통언어 표준등급(CEFR)`을 기준으로 영단어 레벨화
<div>
<img src="https://user-images.githubusercontent.com/33210124/193836104-9f9af9af-48df-490d-99a7-2066b999c47d.gif" width="20%">
<img src="https://user-images.githubusercontent.com/33210124/193836121-90703a08-835c-479a-8873-65fad0025185.gif" width="75%">
</div>
  
### 뉴스 기사 목록
- `선별된 난이도`에 따른 기사 목록 제공 
- `카테고리 대,소분류 필터`를 통한 필터 기사 제공
- 모든 기사 목록 페이지에 `더보기` 구현
<div>
<img src="https://user-images.githubusercontent.com/28249948/193998226-61c3df64-b8a0-436e-9125-d4730a4b4852.gif" width="20%"/>
<img src="https://user-images.githubusercontent.com/28249948/193998218-8a8c0019-7daa-4ee2-a434-5fb1a4a89b69.gif" width="75%"/>
</div>

### 나라별 뉴스 기사 목록
- 대분류 나라별 기사들을 `지구본 상의 마커와 리스트를 통해 시각화`하여 제공
- 나라 선택시 해당 국가의 `상위 언급 키워드`를 오버레이와 해쉬태그 형태로 제공
<div>
<img src="https://user-images.githubusercontent.com/28249948/193990452-452fd2af-54ee-47bc-beb9-a5e2552e0a44.gif" width="20%"/>
<img src="https://user-images.githubusercontent.com/28249948/193992383-23330320-a394-4a17-87d8-a56acdba6097.gif" width="75%"/>
</div>

### 기사 상세 페이지
- `번역`, `TTS`, `스크랩` 기능 제공
- 기사 내 `최다 빈출 단어` 제공 및 저장 기능
- 핵심 단어에서 `TF-IDF` 계산한 결과로 코사인 유사도 계산해 `관련 기사` 제공
 <div>
<img src="https://user-images.githubusercontent.com/33210124/194442218-ce98a729-bc6b-491b-bda7-90284ec2e11b.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/194442222-dccfa564-4a64-4f55-a60e-5e57b72b1394.gif" width="20%">
</div>

### 영어 게임 - 스피드 퀴즈
- 한 문제당 10초의 제한시간을 두고 영단어 맞추기
- 처음 5초는 영어 설명으로 정답 유추
- 이후 5초는 한글 뜻 추가하여 유추
- `사용자 경험을 위해 엔터와 백스페이스를 통한 input 전환`
- 해결 시간에 따른 `뱃지 획득`
- 게임 종료 후 입력 답안 비교, 해당 `단어 추가 기능` 제공
<div>
<img src="https://user-images.githubusercontent.com/33210124/193836088-36f1c2c4-5b83-4e35-acff-3612c02cbee9.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/193836073-8a17f443-9df4-4bf0-8d57-b3d59f920736.gif" width="20%">
</div>
  
### 영어 게임 - 낱말 퍼즐
- `직접 구현한 낱말 퍼즐 생성 알고리즘`을 통해 게임판 생성
- 영어 뜻으로 제공되는 힌트를 보고 가로와 세로 퍼즐 해결
- 사용자 경험을 위해 엔터와 백스페이스를 통한 input 전환
- 게임 종료 후 입력 답안 비교, 해당 `단어 추가 기능` 제공
<div>
<img src="https://user-images.githubusercontent.com/33210124/193836091-939becd8-138f-4a9b-9e0d-d051cee8bf55.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/193836127-ebcc135d-b4b4-4c54-9929-9184a4c600f4.gif" width="20%">
</div>

### 검색
- `키워드, 카테고리 필터, 기간, 레벨`에 따른 기사 검색 결과 제공
- 검색 키워드가 어느 카테고리에 많이 발생했는지 `차트`로 시각적 효과 제공
<div>
<img src="https://user-images.githubusercontent.com/28249948/193999952-9ecf4de8-d9a2-418d-a3b1-608350b914d0.gif" width="75%">
<img src="https://user-images.githubusercontent.com/28249948/193999958-2ff920c2-3794-4fda-abb7-cf402ae0bd9c.gif" width="20%">
</div>

### 오늘의 단어
- 사용자가 오늘 하루 알면 좋은 10개의 단어
- 오늘 발행된 기사 중 `최다 빈출`된 단어 상위 10개를 뽑아 제공
<div>
<img src="https://user-images.githubusercontent.com/33210124/195591727-7c3dceac-528e-4afa-a24e-22a886fccfbf.gif" width="75%">
<img src="https://user-images.githubusercontent.com/33210124/195591721-2a824603-5c87-4b8e-b944-53c367105376.gif" width="20%">
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
- 형상 관리 : Gitlab
- 이슈 관리 : Jira
- 커뮤니케이션 : Zep, Notion
- 디자인 : Figma

**🐳 Backend**
- Python `3.8.0`
- Django `4.2.x`
- Django Rest Framework `3.12.x`
- pipenv or poetry (패키지 관리 도구)
- MySQL (or PostgreSQL) `x.x.x`
- Gunicorn `20.1.0` (배포용 WSGI 서버)
- Swagger (`drf-yasg`)
- Django Rest Framework SimpleJWT (JWT 인증)
- Celery `5.x.x` (비동기 작업 처리)
- Redis `6.x.x` (캐시 및 Celery 브로커)
- Jupyter Notebook `6.4.12`
- Apache Spark `3.2.1`


**🦊 Frontend**
- lang: HTML5, CSS3, JAVASCRIPT

- API
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

### [💭 요구사항 정의 및 기능 명세](https://www.notion.so/newstudy7/e6ffdd72d60d428c90bf8be329c8feeb)

<img width="100%" alt="요구사항 정의 및 기능 명세" src="https://user-images.githubusercontent.com/33210124/192975077-963176ec-93da-4488-97d1-301f60756b59.png"><br>

### [🎨 화면 설계서](https://www.figma.com/file/0O6Jf104BaADRs1zbJ6QJl/%EB%89%B4%EC%8A%A4%ED%84%B0%EB%94%94?node-id=0%3A1)

<img width="100%" alt="화면설계서" src="https://user-images.githubusercontent.com/33210124/192977903-ae783f89-9ea1-4635-9c6e-62bfad14cf00.png"><br>

### [✨ ER Diagram](https://www.erdcloud.com/d/jmYrXGNhwenbvKCCZ)

<img width="100%" alt="erd" src="https://user-images.githubusercontent.com/33210124/194223136-4c18ae2a-445b-4813-a124-e5cef80cf9cc.png" ><br>


# ✨ Conventions 
NEWSTUDY 팀원들의 원활한 `Gitlab`, `Jira` 사용을 위한 [✨컨벤션✨](https://www.notion.so/Conventions-76cebaa0105c4305842d111f3d58352a) 입니다 :)


# 💞 팀원 소개
##### ❤️‍🔥 NEWSTUDY를 개발한 `싸피그룹 영어토익반` 팀원들을 소개합니다!

|**[한윤석](https://github.com/hanyoonseok)**|**[김수빈](https://github.com/kimsubni)**|**[이화연](https://github.com/LeeHwayeon)**|**[육다빈](https://github.com/Dabisix)**|**[윤일준](https://github.com/SmileJune)**|**[정수빈](https://github.com/Soobin07)** |
| :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://avatars.githubusercontent.com/u/28249948?v=4" width="800"> | <img src="https://avatars.githubusercontent.com/u/81076792?v=4" width="800"> | <img src="https://avatars.githubusercontent.com/u/33210124?v=4" width="800"> | <img src="https://avatars.githubusercontent.com/u/80896077?v=4" width="800"> | <img src="https://avatars.githubusercontent.com/u/91049936?v=4" width="800"> | <img src="https://avatars.githubusercontent.com/u/45987276?v=4" width="800"> |
|Leader & Frontend|Frontend|Frontend|Backend|Backend|Backend|

## 😃 팀원 역할

- **한윤석**
  - 팀장, 온보딩, 게임, 기사 상세, 나라별 기사
- **김수빈**
  - 디자인, UCC, 랜딩/기사목록/검색
- **이화연**
  - 회원관리, 다크모드, 마이페이지, 나라별 기사
- **육다빈**
  - 서기, 관련 기사 추천, 데이터 전처리, 단어-카테고리 관련 API
- **윤일준**
  - 배포, 보안, 회원 관련 API, UCC 주연 배우 
- **정수빈**
  - 뉴스 레벨, 워드카운트, 뉴스검색 API

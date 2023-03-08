#  네모난친구들
![image](https://user-images.githubusercontent.com/97939170/223593501-d94afa7c-06d4-47f4-97d8-da29fc854de3.png)

### UCC : [링크]()

### 시연 시나리오 : [링크]()

## ✨Overview
1. 인공지능 기술을 접목한 동물 키우기 게임입니다. 주어진 필드를 자유롭게 꾸미고 나만의 동물과 상호작용 해보세요!

## 팀 소개 : 꾸미는 방법 찾아보기

노은영, 전윤희, 조예지, 최용욱, 추희원, 한진성

## 핵심 서비스

### 먹이주기
![먹이주기](https://user-images.githubusercontent.com/97939170/223593620-74706d26-ea49-423c-aaf0-45bf2c8d63c6.gif)

### 대화하기
![대화하기](https://user-images.githubusercontent.com/97939170/223593658-6048637a-5344-4171-84a4-50fa943a95f6.gif)

### 놀아주기 - 끝말잇기
![끝말잇기](https://user-images.githubusercontent.com/97939170/223593701-3a53f735-c76c-473d-adaa-b887c2cf3d9b.gif)

### 놀아주기 - 미로찾기
![미로찾기](/README.asset/미로찾기.gif)

### 필드 꾸미기
![학생_004_과제_제출](/uploads/d3c93c60a3e82bcc1e6cd7f975e7326a/학생_004_과제_제출.gif)

## 뽑기
![학생_004_과제_제출](/uploads/d3c93c60a3e82bcc1e6cd7f975e7326a/학생_004_과제_제출.gif)

## ✨ 주요 기능
---
- 서비스 설명 : 이미지 분류를 통한 먹이주기, 음성 텍스트 변환(STT)을 이용한 대화하기 등의 기능을 통해 내 동물을 키우고, 그 과정에서 받게 되는 골드를 통해 새 동물이나 조경을 얻어 필드를 꾸밀 수 있습니다.
- 주요 기능 :
    - QuickDraw 데이터셋 을 이용한 낙서 이미지 분류 기능을 통해 동물에게 먹이를 직접 그려서 줄 수 있는 기능
    - STT 모델을 이용한 동물과 대화하기, 끝말잇기 기능
    - 조경을 상점에서 구매하고, 필드에 배치할 수 있는 기능
    - 미로를 돌아다니며 골드를 모을 수 있는 미로찾기 게임

### 개발 환경

---

**Backend**
- Visual Studio Code
- pyton 3.10.5
- Django 3.2.12
- simple jwt
- AWS EC2
- mysql
- redis

**Application**

- Visual Studio Code
- Unity 2020.3.38.f1
- Baracuda 1.0.4


**CI/CD**
- aws ec2
- docker
- nginx
- jenkins

###각 개발 환경 별 포팅 매뉴얼

App : [링크]()

Backend : [링크]()

Embeded : [링크]()

### 아키텍쳐 구성도

---

![아키텍쳐 구성도](/uploads/31a3e7022d4965f7348781040e7f73ac/image.png)

### Jenkins를 이용한 CD 구축 및 SSL 인증서 적용

---

백엔드 CICD 배포 및 SSL 인증서 적용 과정은 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/CICD.md)에서 설명해두었습니다.

### 특이점

---

- Kivy

라즈베리파이의 성능이 기존의 태블릿보다 떨어지기 때문에, 웹을 사용하면 라즈베리파이의 성능상 속도가 매우 느려질 거라고 생각했습니다. 라즈베리 파이에서 사용할 수 있는 App을 구현하는 것을 목표로했고, 관련해서 App 제작을 위한 디자인 툴을 찾아보았습니다. Pyqt는 디자인적으로 부족한 점이 있었고, 그 외 여러 후보군 들 중 Kivy가 원하는 디자인을 만들 수 있다고 판단하여 Kivy를 이용하여 App을 제작하였습니다.

- Quasar : Vue3에서 현재 Vue bootstap이 적용이 안되는 상황에서, Vue3에 특화되어있는 디자인 툴이었기 때문에 사용했습니다. pagenation, modal 등 css만으로는 구현하기 어려운 내용들을 간단하게 구현할 수 있는 컴포넌트들이 많아서, 이를 이용하여 화면을 구성하였습니다.

- Redis

실시간 퀴즈 기능을 구현할 때, 소켓 프로그래밍을 이용하여 웹 -> 임베디드로 신호를 보내어 퀴즈 시작시간을 동기화 하는 방법을 생각했습니다. 이러한 통신을 Django에서 사용하기 위해서는 Redis를 이용해야 한다는 것을 알게 되었고, 도커 컨테이너에 추가하여 Django와 연동했습니다.

- Django-channels

소켓 통신을 위해서 처음에는 파이썬 Websocket 라이브러리를 사용하여 구현을 할 생각이었습니다. 하지만 초기 구현을 진행할 때 막막함이 앞섰고, 개발 전에 장고에서 제공하는 웹 소켓 통신 기능이 있지 않을까 싶어 찾아보던 와중 Django channels를 찾게 되었습니다. Django-channels는 장고의 프로젝트 구조와 유사한 방식으로 소켓 통신을 구현할 수 있도록 지원해줍니다. 이를 이용하여 웹 소켓을 이용한 실시간 퀴즈 기능을 구현하였습니다.

- 배포

Docker, Nginx, Jenkins를 이용하여 무중단 자동 배포를 구축하였습니다. Nginx는 Aws에 서버를 띄워 FE를 서비스했고, Django 서버는 도커의 컨테이너로 넣어 AWS EC2의 Nginx에 도커 프록시로 연결했습니다.



### 협업

---
- Git
- Jira
- Notion
- Mattermost
- Webex
- discode

### 기능 정의서

---
![기능_정의서_1](/uploads/ca30c9aa7193e1a2656f5aa5013e497b/기능_정의서_1.jpg)

![기능_정의서_2](/uploads/c611b84956c82e61dd148eeee7d20392/기능_정의서_2.jpg)

![기능_정의서_3](/uploads/4d89e9feeaa9207aafce54efb568dbc1/기능_정의서_3.jpg)


### 화면 정의서

---

화면 정의서는 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/outputs/%ED%99%94%EB%A9%B4_%EC%A0%95%EC%9D%98%EC%84%9C.pdf)에서 확인해주시기 바랍니다.


### ✨Git 컨벤션

---

```
# <Type> : <제목> 형식으로 작성
# <Type> 영문으로 첫글자 대문자 지켜서 작성
# <제목> 한글로 작성, 제목 끝에 마침표 금지. 무엇을 했는지 1줄로 작성.
#####제목#####

##############
# 아래 공백은 제목과 본문의 분리를 위해 유지

# 본문(추가 설명)이 있는 경우 작성
# 본문은 '어떻게'보다는 '무엇을', '왜' 했는지 설명하기
#####본문#####

##############
# 꼬릿말(footer)을 작성 (관련된 이슈 번호 등 추가)
# 아래 공백은 본문과 꼬릿말의 분리를 위해 유지

# Resolves : 해결 issue
# See also : 참조 및 관련 issue
# 예시) Jira 이슈 S07P12C102-39 해결시 아래와 같이 작성
# Resolves : #39
#####꼬리말#####

#####Type#######
# Feat     : 새로운 기능 추가
# Fix      : 버그 수정
# Docs     : 문서 수정
# Test     : 테스트 코드 추가
# Refactor : 코드 리팩토링
# Style    : 코드 의미에 영향을 주지 않는 변경사항
# Chore    : 빌드 부분 혹은 패키지 매니저 수정사항
################

```

###  ER Diagram

---

![ERD](/uploads/53e58cf572132880d670c9944203a78b/image.png)

- ERD입니다.

### Sequence Diagram

시퀀스 다이어그램은 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/outputs/Sequence%20Diagram.docx)에서 확인하세요!

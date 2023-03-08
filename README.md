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
![꾸미기](https://user-images.githubusercontent.com/97939170/223594854-10e5f3bf-fa6a-4301-96e5-20c33f58c367.gif)

## 뽑기
![뽑기](https://user-images.githubusercontent.com/97939170/223594898-7fb2fba8-931d-474f-87cc-6a9bd94cbae6.gif)

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

### 아키텍쳐 구성도

---

![image](https://user-images.githubusercontent.com/97939170/223594999-76723667-b04a-4428-8d28-9739e7d40d4e.png)

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

### ✨Git 컨벤션

---

## 📌 Commit 규칙

<aside>
💡 **#git이슈번호 종류 - 내용(한국어/영어 상관없음)**

</aside>

**예시)** 


**#31 fix 빌드실패 - blob → recordedBlob**

**#31 feat params fd 하나만 보내지말고 applicantNo 추가해서 백엔드에 보내기**

## 📌 종류 (+[깃모지 추가](https://gitmoji.dev/))

- **feat - 기능 추가**

```
 ✨ :sparkles: 기능 추가 Introduce new features.
```

- **fix - 버그 수정**

```
🐛	:bug:	버그 수정	Fix a bug.
```

- **docs - 문서 수정 (README.md)**

```
📝 :memo: 문서 추가/수정 Add or update documentation.
```

- **style - 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)**

```
🎨 :art: 코드의 구조/형태 개선 Improve structure / format of the code.
```

- **refactor - 코드 리팩토링**

```
♻️ :recycle: 코드 리팩토링 Refactor code.
```

- **test - 테스트 코드**

```
✅ :white_check_mark: 테스트 추가/수정 Add or update tests.
```

- **database - DB 관련 작업**

```
🗃️ :card_file_box: DB 관련 작업 Perform database related changes.
```

- **simple_fix - 심플 이슈 수정**

```
🩹 :adhesive_bandage: 심플 이슈(오타 등) 수정 Simple fix for a non-critical issue.
```

- **comments - 주석**

```
💡 :bulb: 주석 추가 및 수정 Add or update comments in source code.
```

- **catch - 에러 해결**

```
🥅 :goal_net: 에러 잡음 Catch errors.
```

- **chore - 빌드 업무 수정, 패키지 매니저 수정(ex .gitignore 수정 같은 경우)**

```
🙈 :see_no_evil: .gitignore 추가/수정 Add or update a .gitignore file.
```

- **delete - 코드/파일 삭제**

```
🔥 :fire: 코드/파일 삭제 Remove code or files.
```

- **improve - 개선할 필요가 있는 코드**

```
💩  :poop: 똥싼 코드 Write bad code that needs to be improved.
```

`**깃모지 출처**: [https://inpa.tistory.com/entry/GIT-⚡️-Gitmoji-사용법-Gitmoji-cli](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-Gitmoji-%EC%82%AC%EC%9A%A9%EB%B2%95-Gitmoji-cli)`

### 제목

1. 제목과 본문을 `빈 행으로 구분`한다.
2. 제목 첫 글자는 `대문자`로 작성.
3. 제목은 `명령문`으로 사용하며 과거형을 사용하지 않는다.

### 본문

1. `72자 단위로 개행`한다.
2. 양에 구애 받지 않고 `최대한 상세히 작성`
3. 어떻게 했는지 보다는 `무엇을` 바꾸었고 `왜` 바꿨는지 설명

## 📌 GIT FLOW

- Main: 배포
- Develop: BE, FE를 모두 합쳐서 Master 브랜치에 배포
- FrontEnd : Feature합쳐서 develop에 배포
- BackEnd : Feature합쳐서 develop에 배포
- Feature : 각 기능들 (보통 FrontEnd와 BackEnd에서 브랜치가 나눠진다. 예를 들어, 브랜치 이름은 Frontend_기능명으로 통일하기로 한다.)

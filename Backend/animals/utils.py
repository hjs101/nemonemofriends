# date 포맷 형식
date_format_slash = f'%y/%m/%d/%H/%M/%S'


# 전체 명령어 리스트
ALL_COMMANDS = ['', '얘들아']


# 음성 파일 임시 저장
def save_audio(audio):
    fs = FileSystemStorage()
    filename = fs.save(request.user.username +'.wav', audio)

# 음성 파일 삭제
def delete_audio():
    pass


# STT
def speech_to_text(data=None):
    if not data:
        data = "노란아 앉아"
    return data


# gold 보상 처리
def reward_gold(user, action, score=None):
    reward = {'eatting': 100, 'level_up': 777, 'talking_one': 100, 'talking_all': 100, 'playing': 50 * score}
    user.gold += reward[action]
    return user


# exp 보상 처리
def reward_exp(animal, user, action, score=None):
    lookup_grade = [1, 1, 1, 2, 2, 3]  # lookup_grade[level] = grade
    levelup_exp = [0, 0, 100, 200, 300, 400, float('inf')]
    reward = {'eatting': 80, 'talking_one': 50, 'playing': 5 * score}
    
    exp = animal.exp + reward[action]
    next_level = animal.level + 1

    if levelup_exp[next_level] <= exp:
        user = reward_gold(user, 'level_up')
        user.save()
        exp -= levelup_exp[next_level]
        animal.level = next_level
        animal.grade = lookup_grade[next_level]

    animal.exp = exp
    return animal
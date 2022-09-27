<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import TestSerializer, ArraySerializer
from animals.models import Animal
import json
import io
import numpy
# import soundfile as sf

<<<<<<< HEAD
class AudioTestView(APIView):
    def put(self, request):
#         print('request', request)
#         file = request.data.get('vocie')
#         print(file, type(file))
#         # pprint(file.__dir__())
#         print(f'name: {file.name}, file: {file.file}, filed_name: {file.field_name}, content_type: {file.content_type}, charset: {file.charset}, size: {file.size}')
#         with open('media/copy.wav', mode='bx') as f:
#             f.write(audio.file.read()) 
#         a = bytearray(response)
#         f = BytesIO(response)
#         print(f.getvalue())

#         print('response 일부', response[:20], type(response))
#         # print('s일부', s, type(s))
#         # print('a일부', a[:20], type(a))
#         # print('response', response[:20], type(response))
#         # b = numpy.array(a, dtype=numpy.int16)
#         # scipy.io.wavfile.write(r"")
#         # (file: {file.file}, filed_name: {file.field_name}, content_type: {file.content_type}, charset: {file.charset}, size: {file.size}')
#         # print(request.FILES.__dir__())
#         print(request.FILES.keys(), request.FILES.values())
#         # audio = request.FILIES.__getattribute__('file')
#         # print('audio', audio, type(audio))
        pass
=======
from utils import *
from django.core.files.storage import FileSystemStorage
>>>>>>> ec84146 (#5 ✨ 음성 파일 통신 관련 샘플 코드)

class TestView(APIView):
    def post(self,request):
        test_serializer = TestSerializer(data=request.data)
        if test_serializer.is_valid(raise_exception=True):
            test_data = test_serializer.save()
        return Response(test_serializer.data)

class ArrayView(APIView):
    def post(self, request):
        serializer = ArraySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            print(data.column)
        return Response(serializer.data)

class DataAnimals(APIView):
    def post(self, request):
        with open('animals.json', encoding='utf-8') as json_file:
            data = json.load(json_file)['results']
            for animal in data:
                Animal.objects.create(**animal)
            print(type(data))

class AudioView(APIView):
    def post(self, request):
        audio = request.FILES.get("audio")
        print(audio, type(audio))
        # multipart/form-data로 받은 file을 테스트를 위해 bytes로 변환한 후
        # bytes를 wav 파일로 저장

        with open('media/copy.wav', mode='bx') as f:
            f.write(audio.file.read())

        # 서버에 file 저장
        fs = FileSystemStorage()
        filename = fs.save(audio.name, audio)

        # file의 경로
        uploaded_file_path = fs.path(filename)

        # file 삭제
        fs.delete(filename)
<<<<<<< HEAD
        
        return Response(SUCCESS)
=======
=======
>>>>>>> c8733ce (수정)
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import TestSerializer, ArraySerializer
from animals.models import Animal, User_Animal
from accounts.models import WordChain
import json

<<<<<<< HEAD
from utils import *
from animals.utils import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model

from animals.models import Animal, User_Animal
=======
from django.conf import settings

import pickle
from utils import *
from animals.utils import *
from django.core.files.storage import FileSystemStorage
import random
from django.shortcuts import get_object_or_404

# 전처리한 끝말잇기용 단어 목록
with open('noun_dictionary.pickle', 'rb') as f:
    noun_dictionary = pickle.load(f)

# 시작 단어로 쓰기 안 좋은 단어 확인
blacklist = ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '튼', '름', '늠', '쁨']

start_words = []
for word in noun_dictionary:
    if word[0] not in blacklist:
        start_words.append(word)


# 두음 법칙 경우의 수
convert_dict = {
    "라":"나", "락":"낙", "란":"난", "랄":"날", "람":"남", "랍":"납", "랏":"낫", "랑":"낭",
    "략":"약", "량":"양",
    "렁":"넝",
    "려":"여", "녀":"여", "력":"역", "녁":"역",
    "련":"연", "년":"연", "렬":"열", "렴":"염", "념":"염", "렵":"엽", "령":"영", "녕":"영", 
    "로":"노", "록":"녹", "론":"논", "롤":"놀", "롬":"놈", "롭":"놉", "롯":"놋", "롱":"농", 
    "료":"요", "뇨":"요", "룡":"용", "뇽":"용", 
    "루":"누", "룩":"눅", "룬":"눈", "룰":"눌", "룸":"눔", "룻":"눗", "룽":"눙",
    "류":"유", "뉴":"유", "륙":"육", "률":"율", 
    "르":"느", "륵":"늑", "른":"는", "를":"늘", "름":"늠", "릅":"늡", "릇":"늣", "릉":"능", 
    "래":"내", "랙":"낵", "랜":"낸", "랠":"낼", "램":"냄", "랩":"냅", "랫":"냇", "랭":"냉", 
    "례":"예", 
    "뢰":"뇌", 
    "리":"이", "니":"이", "린":"인", "닌":"인", "릴":"일", "닐":"일", "림":"임", "님":"임", "립":"입", "닙":"입", "릿":"잇", "닛":"잇", "링":"잉", "닝":"잉" 
    }

>>>>>>> 3d26de5 (#5 ✨ 끝말잇기)

class TestView(APIView):
    def post(self,request):
        test_serializer = TestSerializer(data=request.data)
        if test_serializer.is_valid(raise_exception=True):
            test_data = test_serializer.save()
        return Response(test_serializer.data)

class ArrayView(APIView):
    def post(self, request):
        serializer = ArraySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
        return Response(serializer.data)

class DataAnimals(APIView):
    def post(self, request):
        # 전체 데이터 생성
        # with open('animals.json', encoding='utf-8') as json_file:
        #     data = json.load(json_file)['results']
        #     for animal in data:
        #         Animal.objects.update(**animal)
        #     print(type(data))

        # 데이터 수정
        with open('animals.json', encoding='utf-8') as json_file:
            data = json.load(json_file)['results']
            for i in range(len(data)):
                print(Animal.objects.filter(id=i+1).update(**data[i]))


class AudioView(APIView):
<<<<<<< HEAD
<<<<<<< HEAD
    # 전체 동물 대화
    def talk_to_all(self, context, user):
        print('길이', len(ALL_COMMANDS))
        for i in range(1, len(ALL_COMMANDS)):
            if ALL_COMMANDS[i] in context:
                if not user.is_called:
                    user = reward_gold(user, 'talking_all')
                    user.is_called = True
                    user.save()
                response = {'animal_id': -1, 'cmd': i}
                response.update(SUCCESS)
                return response
        return FAIL

    # 특정 동물 대화
    def talk_to_one(self, animal, user, context):
        action = 'talking_one'
        grade = animal.grade
        commands = animal.animal.commands[:grade+1]

        for i in range(1, len(commands)):
            if commands[i] in context:
                # 대화 보상 Ok
                if animal.talking_cnt:
                    animal = reward_exp(animal, user, action)
                    animal.talking_cnt -= 1
                    animal.save()
                    user = reward_gold(user, action)
                    user.save()
                # 대화 보상 No
                response = {'animal_id': animal.animal_id, 'cmd': i}
                response.update(SUCCESS)
                return response
        return FAIL

    def post(self, request):
<<<<<<< HEAD
=======
    def put(self, request):
=======
    def post(self, request):
>>>>>>> 20f175f (다시 post로 복구)
        print(request.FILES)
>>>>>>> 3d256b3 (post put으로 변경)
        audio = request.FILES["audio"]
        
        # multipart/form-data로 받은 file을 테스트를 위해 bytes로 변환한 후
        # bytes를 wav 파일로 저장
<<<<<<< HEAD
=======
        audio = request.FILES["audio"]

        # multipart/form-data로 받은 file을 테스트를 위해 bytes로 변환한 후
        # bytes를 wav 파일로 저장
>>>>>>> 3d26de5 (#5 ✨ 끝말잇기)
        with open('media/copy.wav', mode='bx') as f:
            f.write(audio.file.read())
=======

        # with open('media/copy.wav', mode='bx') as f:
            # f.write(audio.file.read())
>>>>>>> 0df669a (음성 데이터 유저 네임으로 저장)

        # 서버에 file 저장
        fs = FileSystemStorage()
        filename = fs.save(request.user.username +'.wav', audio)
        # filename = fs.save(request.user, audio)
        # filename = fs.save(audio.name, audio)

        # 로직        
        context = '꼬꼬 앉아'
        # file의 경로
        uploaded_file_path = fs.path(filename)

        # file 삭제
<<<<<<< HEAD
<<<<<<< HEAD
        fs.delete(filename)
<<<<<<< HEAD
<<<<<<< HEAD
        
        return Response(SUCCESS)
>>>>>>> 1e971fb (#4 put -> post)
=======
        fs.delete('copy.wav')
        return Response(SUCCESS)
>>>>>>> 1ad1ed3 (수정)
=======
        fs.delete(settings.BASE_DIR + '/copy.wav')
        return Response(SUCCESS)
>>>>>>> 70af774 (settings.BASE_DIR 추가)
=======
        fs.delete(settings.MEDIA_ROOT + '/copy.wav')
        
        return Response(SUCCESS)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8112dd7 (MEDIA_ROOT 추가)
=======
        # fs.delete(filename)
        # fs.delete(settings.MEDIA_ROOT + '/copy.wav')
        return Response(SUCCESS)
>>>>>>> 0df669a (음성 데이터 유저 네임으로 저장)
=======
        fs.delete(filename)
        fs.delete(settings.MEDIA_ROOT + f'/{filename}.wav')

        user = get_object_or_404(get_user_model(), username=request.user)
        user_animals = get_list_or_404(User_Animal, user=user)

        for animal in user_animals:
            if animal.name in context:
                print('animal', animal, 'animla.name', animal.name, '?', context)
                response = self.talk_to_one(animal, user, context)
                return Response(response)

        print("TEST", context, user)
        response = self.talk_to_all(context, user)
        return Response(response)



        response = SUCCESS.copy()


        return Response(SUCCESS)
>>>>>>> 6d6c027 (#4 ✨ 대화 - "꼬꼬 앉아" 테스트)
=======
>>>>>>> 3d256b3 (post put으로 변경)
=======

class PlayWordchainStartView(APIView):
    def post(self, request):
        user = request.user
        animal_id = request.data.get('animal_id')
        animal = get_object_or_404(Animal, pk=animal_id)
        user_animal = get_object_or_404(User_Animal, user=user, animal=animal)

        if user_animal.playing_cnt < 1:
            response = FAIL.copy()
            response.update({'message': '오늘은 더 이상 놀아줄 수 없습니다.'})
            return Response(response)

        response_word = random.choice(start_words)

        # 삭제되지 않은 게임 기록 확인
        check = WordChain.objects.filter(user=user)
        if check:
            for wordchain in check:
                wordchain.delete()
            
        wordchain = WordChain(user=user, score=0, words=[response_word])
        wordchain.save()

        response = SUCCESS.copy()
        response.update({'response_word': response_word})

        return Response(response)

class PlayWordchainNextView(APIView):
    # 게임 종료
    def finish(self, msg, score, request_word):
        response = FAIL.copy()
        response.update({'message': msg, 'request_word': request_word, 'score': score})
        return response

    def post(self, request):
        # audio = request.FILES['audio']
        # fss = FileSystemStorage()
        # filename = fss.save(request.user.username +'.wav', audio)
        # filepath = fss.path(filename)

        # # 음성 인식
        # # request_word = recognize(filepath)
        # request_word = '단어'

        # fss.delete(settings.MEDIA_ROOT + f'/{filename}.wav')
        request_word = recongize(request.user.username, request.FILES['audio'])
        wordchain = WordChain.objects.get(user_id=request.user)
        words = wordchain.words
        score = wordchain.score
        
        # 사용자의 단어가 사전에 존재하는 단어인지 확인
        if request_word not in noun_dictionary:
            response = self.finish('사전에 존재하지 않는 단어입니다.', score, request_word)
            return Response(response)

        # 사용자의 단어가 이미 사용한 단어인지 확인
        if request_word in words:
            response = self.finish('이미 사용한 단어입니다.', score, request_word)
            return Response(response)

        # 사용자의 단어가 실제로 이어지는 단어인지 확인(두음 법칙 적용)
        ends = [words[-1][-1]]
        if ends[0] in convert_dict.keys():
            ends.append(convert_dict[ends[0]])

        if request_word[0] not in ends:
            response = self.finish('이어지지 않는 단어입니다.', score, request_word)
            return Response(response)
        
        # 시작 글자로 쓸 수 있는 글자들 확인(두음 법칙 적용)
        starts = [request_word[-1]]
        if starts[0] in convert_dict.keys():
            starts.append(convert_dict[starts[0]])
        
        # 다음 단어 선택
        response_words = []
        for word in noun_dictionary:
            if word[0] in starts and word not in words:
                response_words.append(word)
        
        response_word = random.choice(response_words)
        
        # WordChain 테이블 갱신
        wordchain.score += 1
        wordchain.words.append(request_word)
        wordchain.words.append(response_word)
        wordchain.save()

        response = SUCCESS.copy()
        response.update({'request_word': request_word, 'response_word': response_word, 'score': wordchain.score})
        return Response(response)

class PlayWordchainFinishView(APIView):
    def post(self, request):
        user = request.user
        wordchain = WordChain.objects.get(user=user)
        score = wordchain.score
        animal_id = request.data.get('animal_id')
        animal = get_object_or_404(Animal, pk=animal_id)
        user_animal = get_object_or_404(User_Animal, user=user, animal=animal)
        action = 'playing'

        # 골드 증가
        user = reward_gold(user, action, score)
        user.save()

        # 놀이 횟수 차감
        user_animal.playing_cnt -= 1

        # 해당 동물 경험치 증가
        user_animal = reward_exp(user_animal, user, action, score)
        user_animal.save()

        # wordchain에서 행 삭제
        wordchain.delete()

        return Response(SUCCESS)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3d26de5 (#5 ✨ 끝말잇기)
=======
>>>>>>> 35545c1 (#5 🐛 사용자로부터 받은 음성 파일 저장 및 삭제 수정)
=======


from django.core.cache import cache

class CacheView(APIView):
    def post(self, request):
        user = request.user
        cache.set(user.username, [0, '제시어'], 60 * 60)
        test = cache.get(user.username)
        test[0] = 1
        test.append('단어')
        ttest = cache.get(user.username)
        print(ttest)
        return Response(SUCCESS)
>>>>>>> c2c0a0d (#5 ♻️ 끝말잇기 Redis 적용)

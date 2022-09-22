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
from animals.models import Animal
import json

from utils import *
from animals.utils import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model

from animals.models import Animal, User_Animal

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
        audio = request.FILES["audio"]
        
        # multipart/form-data로 받은 file을 테스트를 위해 bytes로 변환한 후
        # bytes를 wav 파일로 저장
<<<<<<< HEAD
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

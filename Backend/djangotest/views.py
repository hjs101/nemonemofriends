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
from django.core.files.storage import FileSystemStorage

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
        
        return Response(SUCCESS)
>>>>>>> 1e971fb (#4 put -> post)
=======
        fs.delete('copy.wav')
        return Response(SUCCESS)
>>>>>>> 1ad1ed3 (수정)

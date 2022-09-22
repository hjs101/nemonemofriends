"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.TestView.as_view(), name='test'),
    path('array/', views.ArrayView.as_view(), name='array'),
    path('data_animals/', views.DataAnimals.as_view()),
<<<<<<< HEAD
    path('audiotest/', views.AudioTestView.as_view()),
=======
    path('audio/', views.AudioView.as_view()),
<<<<<<< HEAD
>>>>>>> ec84146 (#5 ✨ 음성 파일 통신 관련 샘플 코드)
=======
    path('play/wordchain/start/', views.PlayWordchainStartView.as_view()),
    path('play/wordchain/next/', views.PlayWordchainNextView.as_view()),
    path('play/wordchain/finish/', views.PlayWordchainFinishView.as_view()),
>>>>>>> 3d26de5 (#5 ✨ 끝말잇기)
]

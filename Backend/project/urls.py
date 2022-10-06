<<<<<<< HEAD
<<<<<<< HEAD
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('djangotest.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    path('accounts/', include('accounts.urls')),
=======
    path('animals/', include('animals.urls')),
>>>>>>> 57add71 (#5 ✨ animals 요청 분기)
=======
    path('items/', include('items.urls')),
>>>>>>> e2b459e (#2 :sparkles: 조경 배치, 구매)
]
=======
=======
>>>>>>> aabf203 (Fix items models.py)
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
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('accounts/', include('accounts.urls')),
<<<<<<< HEAD
]
>>>>>>> 9ba888b (Update urls.py)
=======
    path('animals/', include('animals.urls')),
<<<<<<< HEAD
]
>>>>>>> aabf203 (Fix items models.py)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> ec84146 (#5 ✨ 음성 파일 통신 관련 샘플 코드)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 330c239 (#4 🐛 병합 잔해 제거)
"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d0xo-huf@-+5k=c+4y*h*i+q#iom6y*e_ud=afm48r5qedq*t8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD
<<<<<<< HEAD
    # local apps
    'accounts',
=======
=======
    # local apps
    'accounts',
    'animals',
    'djangotest',
    'items',

    # 3rd party 라이브러리
    'rest_framework',
    'rest_framework.authtoken',
    'django_apscheduler',

    # DRF auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    # signup 위해 필요
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # django 내장
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Django 스케쥴러 관련 설정
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

SCHEDULER_DEFAULT = True

# 로그인, 인증 관련 설정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    # 로그인 할 때 헤더에서 jwt 토큰 유효한지 확인하는 설정
    # 'DEFAULT_PERMISSION_CLASSES' : [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD= 'username'
AUTH_USER_MODEL = 'accounts.User'
REST_USE_JWT = True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),
    'ROTATE_REFRESH_TOKENS': False,
    'USER_ID_FIELD': 'username',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Medai files (caching wav file for STT)
MEDIA_URL = '/media/'


# Logging
# https://wikidocs.net/77522
# https://devlink.tistory.com/355

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 포맷터 (텍스트의 포맷 형식 정의, 여러 포맷 정의 가능)
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    'filters': {
        # 'require_debug_false': {
        #     '()': 'django.utils.log.RequireDebugFalse',
        # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 핸들러 (로그 레코드로 무슨 작업을 할 것인지 정의, 여러 핸들러 정의 가능)
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'INFO',
            # 'filters': ['require_debug_false', 'require_debug_true'],
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'files/log/logfile.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'format1',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },
    'loggers': {
        # 로거 종류
        'django.request': {
            'handlers':['file'],
            'propagate': False,
            'level':'INFO',
        },
        # 사용자 APP 지정
        'animals': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'INFO',
        },
        'accounts': {
            'handlers': ['file'],
            'propagate': False,
            'level': 'INFO',
        },
    },
<<<<<<< HEAD
}

"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d0xo-huf@-+5k=c+4y*h*i+q#iom6y*e_ud=afm48r5qedq*t8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # local apps
    'accounts',
>>>>>>> 330c239 (#4 🐛 병합 잔해 제거)
    'animals',
>>>>>>> 54ea8f5 (💩 임시저장)
    'djangotest',
<<<<<<< HEAD
<<<<<<< HEAD
    # 3rd party apps
=======
    'items',
>>>>>>> e2b459e (#2 :sparkles: 조경 배치, 구매)
=======
    'items',

    # 3rd party 라이브러리
>>>>>>> 6776c8e (💡 주석 수정)
    'rest_framework',
    'rest_framework.authtoken',
    'django_apscheduler',
    # DRF auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    # signup 위해 필요
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # django 내장
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Django 스케쥴러 관련 설정
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

SCHEDULER_DEFAULT = True

# 로그인, 인증 관련 설정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    # 로그인 할 때 헤더에서 jwt 토큰 유효한지 확인하는 설정
    # 'DEFAULT_PERMISSION_CLASSES' : [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD= "username"
AUTH_USER_MODEL = 'accounts.User'
REST_USE_JWT = True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'USER_ID_FIELD': 'username',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')


# Logging
# https://wikidocs.net/77522
# https://devlink.tistory.com/355

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 포맷터 (텍스트의 포맷 형식 정의, 여러 포맷 정의 가능)
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 핸들러 (로그 레코드로 무슨 작업을 할 것인지 정의, 여러 핸들러 정의 가능)
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false', 'require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'files/log/logfile.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'format1',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },
    'loggers': {
        # 로거 종류
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers':['file'],
            'propagate': True,
            'level':'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        # 사용자 APP 지정
        'animals': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'accounts': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'items': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
    },
<<<<<<< HEAD
}
=======
"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d0xo-huf@-+5k=c+4y*h*i+q#iom6y*e_ud=afm48r5qedq*t8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # local apps
    'accounts',
    'animals',
    'djangotest',
    'items',

    # 3rd party 라이브러리
    'rest_framework',
    'rest_framework.authtoken',
    'django_apscheduler',
    # DRF auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    # signup 위해 필요
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # django 내장
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Django 스케쥴러 관련 설정
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

SCHEDULER_DEFAULT = True

# 로그인, 인증 관련 설정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    # 로그인 할 때 헤더에서 jwt 토큰 유효한지 확인하는 설정
    # 'DEFAULT_PERMISSION_CLASSES' : [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
}

STATE = env('STATE')
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD= "username"
AUTH_USER_MODEL = 'accounts.User'
REST_USE_JWT = True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'USER_ID_FIELD': 'username',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')


# Logging
# https://wikidocs.net/77522
# https://devlink.tistory.com/355

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 포맷터 (텍스트의 포맷 형식 정의, 여러 포맷 정의 가능)
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
    },
    # 핸들러 (로그 레코드로 무슨 작업을 할 것인지 정의, 여러 핸들러 정의 가능)
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'files/log/logfile.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'format1',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },
    'loggers': {
        # 로거 종류
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers':['file'],
            'propagate': True,
            'level':'INFO',
        },
        # 사용자 APP 지정
        'animals': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'accounts': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'items': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
    },
}
>>>>>>> 91ece6c (Update Backend/project/settings.py)
=======
}
>>>>>>> feac533 (♻️ settings.py 중복 제거)
=======
}


# Cache -- Redis
# https://funncy.github.io/django/2020/09/24/redis/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://j7c201.p.ssafy.io:6379/1", # 1번 DB
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
>>>>>>> c2c0a0d (#5 ♻️ 끝말잇기 Redis 적용)

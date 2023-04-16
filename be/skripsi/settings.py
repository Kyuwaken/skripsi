"""
Django settings for skripsi project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2y-=!zk%upvb$%j3xm01g9k@ajb_g6q0+imnt$o3m@nz6ttjje'

# set 20 MB for uploading data, on default 5 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECRET_KEY = '4aEZPz1CoUWbujbe-_lYERfZuV_bSatnFj4y_R2L1W0='
SECRET_KEY = '6c33d4abde09fe1c4ac9b76f245d7df4'
IV = 'ddc5b6c4d6e4b6c4'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = []

ENV_VARIABLE = {
    'MAX_LEVEL_INCLUDE': 5,
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'django_softdelete',
    # buat allow origin
    'corsheaders'
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'api.exceptions.custom_exception_handler.custom_exception_handler'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # buat allow origin
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # custom middleware
    'api.middleware.custom_auth_middleware.CustomAuthMiddleware',
    # 'api.middleware.custom_request_log_middleware.RequestLogMiddleware',
]

# buat allow origin
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'skripsi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'skripsi.wsgi.application'

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "root": {"level": "INFO", "handlers": ["file"]},
#     "handlers": {
#         "file": {
#             "level": "INFO",
#             "class": "logging.FileHandler",
#             "filename": "django.log",
#             "formatter": "custom_json",
#         },
#         'gunicorn': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             "formatter": "custom_json",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file",'gunicorn'],
#             "level": "INFO",
#             "propagate": True
#         },      
#     },
#     "formatters": {
#         "app": {
#             "format": (
#                 u"%(asctime)s [%(levelname)-8s] "
#                 "(%(module)s.%(funcName)s) %(message)s"
#             ),
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },        
#         'verbose': {
#             'format': ' "message" : {message} ,"level" : {levelname} ',
#             'style': '{',
#         },
#         'custom_json' :{
#             '()' : CustomJsonFormatter
#         }
#     },
# }


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# host_names = str(os.getenv('host'))
# user_names = str(os.getenv('user'))
# password_names = str(os.getenv('password'))
# port_names = str(os.getenv('port'))
# db_names = str(os.getenv('name'))

schema_skripsi = "public"
host_names = "localhost"
user_names = "postgres"
password_names = "ian012"
port_names = "5432"
db_names = "postgres"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path={}'.format(schema_skripsi)
        },
        'NAME': db_names,
        'USER': user_names,
        'PASSWORD': password_names,
        'HOST': host_names,
        'PORT': port_names,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

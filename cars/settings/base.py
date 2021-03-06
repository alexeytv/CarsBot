
import os
from decouple import config, Csv
from pathlib import Path

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'django_telegrambot',
    'mapwidgets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cars.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'cars.wsgi.application'


# Password validation

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MAP_WIDGETS = {
    "GOOGLE_MAP_API_KEY": config('GOOGLE_MAP_API_KEY'),
    "LANGUAGE": "ru"
}

# Telegram
DJANGO_TELEGRAMBOT = {
    'MODE': 'POLLING',
    'BOTS': [
        {
            'TOKEN': config('TELEGRAM_BOT_TOKEN'),
        },
    ],

}

# Bot/email message
MESSAGE_TEMPLATE_EMAIL = Path(os.path.join(BASE_DIR, 'messages/message_email.html')).read_text()
MESSAGE_TEMPLATE_BOT = Path(os.path.join(BASE_DIR, 'messages/message_bot.txt')).read_text()

MESSAGE_HELP = Path(os.path.join(BASE_DIR, 'messages/message_help.txt')).read_text()
MESSAGE_START = Path(os.path.join(BASE_DIR, 'messages/message_start.txt')).read_text()

MAIL_SUBJECT = Path(os.path.join(BASE_DIR, 'messages/message_subject.txt')).read_text()

WEBSITE_LINK = config('WEBSITE_LINK', default='http://localhost:8000')

EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = config('EMAIL_PORT', default=465)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

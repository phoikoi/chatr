import sys, os
from .config import load_config, config, config_int, config_list, config_bool

if sys.version_info < (3, 6):
    raise RuntimeError("chatr requires python >= 3.6.0")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_config(os.path.join(BASE_DIR,'site.ini'))

SECRET_KEY = config('django.secret_key')

DEBUG = config_bool('django.debug_mode', default=False)
CACHE_ON = config_bool('django.cache_on', default=False)
ALLOWED_HOSTS = config_list('django.allowed_hosts', default='*')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
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

ROOT_URLCONF = 'chatr.urls'

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

WSGI_APPLICATION = 'chatr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('db.name', default='chatr'),
        'USER': config('db.user', default='chatr'),
        'PASSWORD': config('db.password', default='chatr'),
        'HOST': config('db.host', default='127.0.0.1'),
        'PORT': config_int('db.port', default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "ROUTING": "chatr.routing.channel_routing",
        "CONFIG": {
#            "hosts": [("redis-channel-1", 6379)],
        },
    },
}

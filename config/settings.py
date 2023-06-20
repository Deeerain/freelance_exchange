from pathlib import Path
from django.utils.translation import gettext_lazy as _
from os import environ


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ\
    .get('SECRET_KEY',
         'django-insecure-n6_(76%h#q-#*5msk8-=amoe9*&l700^me$z5edpf+hl*ro39=')

DEBUG = int(environ.get('DEBUG', 1))

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '127.0.0.1').split()

INTERNAL_IPS = environ.get('INTERNAL_IPS', '127.0.0.1').split()


INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'django_elasticsearch_dsl',
    'burse',
    'accounts',
    'tasks',
    'replays',
    'chatting',
    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = 'config.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

DATABASES = {
    'default': {
        'ENGINE': environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': environ.get('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': environ.get('DB_USER', 'django'),
        'PASSWORD': environ.get('DB_PASSWORD', 'django'),
        'HOST': environ.get('DB_HOST', 'localhost'),
        'PORT': environ.get('DB_PORT', 5432),
    }
}

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

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = 'tasks:list'

LOGOUT_REDIRECT_URL = 'burse:home'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("ru", _("Russian")),
    ("en", _("English")),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BURSE_ROLES = [
    'Executor',
    'Customer',
]

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': environ.get('ELASTICSEARCH_DSL', 'localhost:9200').split()
    },
}

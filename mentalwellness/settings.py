"""
Django settings for mentalwellness project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<SECRET_KEY>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
                 '.localhost', '[::1]']

# Application definition

INSTALLED_APPS = [
    'styletransfer.apps.StyletransferConfig',
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mentalwellness.urls'

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

WSGI_APPLICATION = 'mentalwellness.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

CONNECT_TO_DB = False

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # postgres
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DB_NAME>',
        'USER': 'postgres',
        'PASSWORD': '<DB_PASSWORD>',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Media files (Images, Videos)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

PREDICTION_MODEL_URL = {
    'stargan': {
        'HOST': '<STARGAN_IP>',
        'PORT': '<STARGAN_PORT>',
        'ENDPOINT': '<STARGAN_ENDPOINT>'
    },
    'simswap': {
        'HOST': '<SIMSWAP_IP>',
        'PORT': '<SIMSWAP_PORT>',
        'ENDPOINT': '<SIMSWAP_ENDPOINT>'
    }
}

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s.%(msecs)03d] %(levelname)s in %(module)s: %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        }},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'level': 'INFO'
        },  'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': './logs/log.txt',
            'level': 'DEBUG',
            'when': 'D',
            'backupCount': 30
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
}

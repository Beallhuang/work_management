'''
Description: 
Author: beallhuang
Date: 2024-06-28 15:09:14
LastEditTime: 2024-07-02 11:43:04
LastEditors: beallhuang
'''
"""
Django settings for belle_management project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from .db_config import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rc(nbc8a=+%&vr(fv3+fdlo37cgqf%avsc^312dt2d+yv5(!14"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False   

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "files.apps.FilesConfig",
    "index_change.apps.IndexChangeConfig",
    "fileapp.apps.FileappConfig",
    "industry_report_upload.apps.IndustryReportUploadConfig",
    "live_refund_monitor.apps.LiveRefundMonitorConfig",
    "middlewares.apps.MiddlewaresConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'middlewares.PermissionMiddleware.PermissionMiddleware',  # 添加自定义中间件
    'middlewares.LogMiddleware.OpLogs',  # 添加自定义中间件
]


ROOT_URLCONF = "belle_management.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "belle_management.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST':db_host,
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# BASE_DIR 是项目的绝对地址
# STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
STATIC_ROOT = '/home/huang.biao/http_app/Django/belle_management/collect_static'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, STATIC_URL),
# ]

# # Default primary key field type
# # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

# 设置右上角Home图标跳转链接，以另外一个窗口打开
SIMPLEUI_INDEX = 'http://127.0.0.1:8000/admin'

SIMPLEUI_LOGO = 'http://127.0.0.1:8000/static/admin/img/logo.jpg'



# 清除图片插件, 多选枚举插件
INSTALLED_APPS = INSTALLED_APPS + ['django_cleanup.apps.CleanupConfig', 'multiselectfield']

# socket配置
INSTALLED_APPS += [
    'channels',
]

ASGI_APPLICATION = 'belle_management.asgi.application'

# 配置 Redis 作为 Channels 的通信层
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],  # Redis 地址
        },
    },
}
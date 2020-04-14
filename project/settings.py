"""
Django settings for life.zackzhang.net project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# production.py 只放在服务器端
try:
    from production import secret_key
    # 生产环境
    debug_mode = False
except ImportError:
    # 开发环境
    debug_mode = True


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "6-xi@v5hu7^)z@==9%x4ca-h+99i=cj+f!!04$cpys_)y7to^=" if debug_mode else secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug_mode

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'life.zackzhang.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'comment',
    'about',
    'status',
    'music',
    "rest_framework",
    "rest_framework.authtoken",
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 在服务器端运行 collectstatic 将静态文件收集到的位置（根目录下的 static 文件夹）
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 在 HTML 模板中引用静态文件添加的前缀（i.e. {% static ... %}）
STATIC_URL = '/static/'

# 除每个 app 中，静态文件的其他位置（用于放 app 共用的静态文件）
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'common', 'static')]

# Django REST framework 全局设置

drf_auth_classes = ["rest_framework.authentication.TokenAuthentication"]
drf_rend_classes = ["rest_framework.renderers.JSONRenderer"]
if debug_mode:
    # 开发环境下方便浏览器查看
    drf_auth_classes.insert(0, "rest_framework.authentication.BasicAuthentication")
    drf_auth_classes.insert(1, "rest_framework.authentication.SessionAuthentication")
    drf_rend_classes.append("rest_framework.renderers.BrowsableAPIRenderer")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": drf_auth_classes,
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAdminUser"],
    "DEFAULT_RENDERER_CLASSES": drf_rend_classes,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 如果低于 10 项就不分页
    'PAGE_SIZE': 10,
}

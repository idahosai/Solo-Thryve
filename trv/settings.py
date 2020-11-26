"""
Django settings for trv project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from django.contrib.messages import constants as messages
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wn^s8d-of-*9@w@&2nt8-1kf$*p2$+fc8ihb8oct3is8^50-dp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://web-app-thrv.us-east-2.elasticbeanstalk.com', 'web-app-thrv.us-east-2.elasticbeanstalk.com',
                 'localhost', '172.31.1.170', '127.0.0.1', '172.31.28.160', 'localhost']


# Application definition
BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'

BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap'
)

INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'appointments.apps.AppointmentsConfig',
    'accountmanagement.apps.AccountmanagementConfig',
    'data_analysis.apps.DataAnalysisConfig',
    'staff.apps.StaffConfig',
    'dashboard.apps.DashboardConfig',
    'students.apps.StudentConfig',
    'program.apps.SchoolprogramConfig',
    'student.apps.StudentAccountConfig',
    'studentauth.apps.StudentauthConfig',
    'careerform.apps.CareerformConfig',
    'studentdata.apps.StudentdataConfig',
    'employmentform.apps.EmploymentformConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'schedule',
    'djangobower',
    'rest_framework',
    "form.apps.FormConfig",
    'widget_tweaks',
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

ROOT_URLCONF = 'trv.urls'

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
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'trv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'thryvedatabase',
        'USER': 'thryve2020',
        'PASSWORD': 'Thryve2020!',
        'HOST': 'thryve-database-2020.clkzzm3gdrpr.us-east-2.rds.amazonaws.com'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'trv/static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Email config

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST: 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'mobeenraza39@gmail.com'
# EMAIL_HOST_PASSWORD = 'nqdqhstoueyuuhfw'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

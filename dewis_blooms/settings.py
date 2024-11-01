import os
import environ
import dj_database_url

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security Settings
SECRET_KEY = env("SECRET_KEY", default='your-default-secret-key')  # Replace for security
DEBUG = env.bool("DEBUG", default=False)

# Allowed Hosts
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'dewis-blooms.herokuapp.com',
    '8000-ashwinsel-milestoneproj-gw7p0d2mufe.ws.codeinstitute-ide.net'
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-ashwinsel-milestoneproj-gw7p0d2mufe.ws.codeinstitute-ide.net',
    'https://*.herokuapp.com'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'shop',
    'products',
    'storages',
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-allauth configurations
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
LOGIN_URL = '/accounts/login/'
ACCOUNT_LOGOUT_ON_GET = True
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'dewis_blooms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dewis_blooms.wsgi.application'

# Database Configuration (Switching from SQLite to PostgreSQL in production)
DATABASES = {
    'default': dj_database_url.config(
        default=env("DATABASE_URL", default='postgres://utilh44h3i6:LdtNQVOJUT2v@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/wired_blimp_cage_401071'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and Media files configuration (for local development)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# S3 Storage for Static and Media Files in Production
if not DEBUG:
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")

    # Tell Django to use S3 for file storage in production
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
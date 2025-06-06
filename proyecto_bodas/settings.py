# proyecto_bodas/settings.py
"""
Django settings for proyecto_bodas project.
Generated by 'django-admin startproject' using Django 5.2.1.
"""

from pathlib import Path
import os
from dotenv import load_dotenv  # Para cargar variables de entorno

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ejecutar carga de variables del .env
# Asegúrate de que el archivo .env esté en la misma carpeta que manage.py
load_dotenv(os.path.join(BASE_DIR, '.env')) # Especificar ruta completa al .env es más robusto

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r)k0v=9pfmk8svkzsed2&_#-(2+78mkeh)!-g+n%6+xe+*yinr' # [cite: 1, 2, 3]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # [cite: 1, 2, 3]

ALLOWED_HOSTS = [] # [cite: 1, 2, 3]


# Application definition

INSTALLED_APPS = [ # [cite: 1, 2, 3]
    'django.contrib.admin', # [cite: 1, 2, 3]
    'django.contrib.auth', # [cite: 1, 2, 3]
    'django.contrib.contenttypes', # [cite: 1, 2, 3]
    'django.contrib.sessions', # [cite: 1, 2, 3]
    'django.contrib.messages', # [cite: 1, 2, 3]
    'django.contrib.staticfiles', # [cite: 1, 2, 3]
    'core', # [cite: 1, 2, 3]
]

MIDDLEWARE = [ # [cite: 1, 2, 3]
    'django.middleware.security.SecurityMiddleware', # [cite: 1, 2, 3]
    'django.contrib.sessions.middleware.SessionMiddleware', # [cite: 1, 2, 3]
    'django.middleware.common.CommonMiddleware', # [cite: 1, 2, 3]
    'django.middleware.csrf.CsrfViewMiddleware', # [cite: 1, 2, 3]
    'django.contrib.auth.middleware.AuthenticationMiddleware', # [cite: 1, 2, 3]
    'django.contrib.messages.middleware.MessageMiddleware', # [cite: 1, 2, 3]
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # [cite: 1, 2, 3]
]

ROOT_URLCONF = 'proyecto_bodas.urls' # [cite: 1, 2, 3]

TEMPLATES = [ # [cite: 1, 2, 3]
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # [cite: 1, 2, 3]
        'DIRS': [], # [cite: 1, 2, 3]
        'APP_DIRS': True, # [cite: 1, 2, 3]
        'OPTIONS': { # [cite: 1, 2, 3]
            'context_processors': [ # [cite: 1, 2, 3]
                'django.template.context_processors.request', # [cite: 1, 2, 3]
                'django.contrib.auth.context_processors.auth', # [cite: 1, 2, 3]
                'django.contrib.messages.context_processors.messages', # [cite: 1, 2, 3]
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_bodas.wsgi.application' # [cite: 1, 2, 3]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = { # [cite: 1, 2, 3]
    'default': { # [cite: 1, 2, 3]
        'ENGINE': 'django.db.backends.sqlite3', # [cite: 1, 2, 3]
        'NAME': BASE_DIR / 'db.sqlite3', # [cite: 1, 2, 3]
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ # [cite: 1, 2, 3]
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # [cite: 1, 2, 3]
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # [cite: 1, 2, 3]
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # [cite: 1, 2, 3]
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # [cite: 1, 2, 3]
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'es-cl' # [cite: 1, 2]
TIME_ZONE = 'America/Santiago' # [cite: 1, 2]
USE_I18N = True # [cite: 1, 2, 3]
USE_TZ = True # [cite: 1, 2, 3]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/' # [cite: 1, 2, 3]
STATICFILES_DIRS = [ # [cite: 1]
    BASE_DIR / "core" / "static", # [cite: 1]
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # [cite: 1, 2, 3]

# Configuración de archivos multimedia (subidos por el usuario)
MEDIA_URL = '/media/' # [cite: 1, 2, 3]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # [cite: 1, 2, 3]

# --- CONFIGURACIÓN DE CORREO ELECTRÓNICO USANDO GMAIL (LEYENDO DE .ENV) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # [cite: 1]
EMAIL_HOST = 'smtp.gmail.com'  # Para Gmail [cite: 1]
EMAIL_PORT = 587               # Puerto para TLS con Gmail [cite: 1]
EMAIL_USE_TLS = True           # Gmail usa TLS [cite: 1]
# EMAIL_USE_SSL = False        # No necesario si EMAIL_USE_TLS es True [cite: 1]

# Lee las credenciales desde el archivo .env
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER_GMAIL') # [cite: 1]
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD_GMAIL') # Tu contraseña de aplicación de 16 caracteres [cite: 1]

# El correo que aparecerá como remitente en los correos.
# Es buena práctica que sea el mismo que EMAIL_HOST_USER o un alias configurado.
# Usamos un fallback al EMAIL_HOST_USER si DEFAULT_FROM_EMAIL_GMAIL no está en .env
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL_GMAIL', EMAIL_HOST_USER) # [cite: 1]

# Opcional: Para que los errores de Django se envíen a estos correos si DEBUG = False
# ADMINS = [('Tu Nombre Admin', EMAIL_HOST_USER)] # Ejemplo usando la variable leída [cite: 1]

# --- FIN CONFIGURACIÓN DE CORREO ---
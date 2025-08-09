from mysite.settings import *

# production settings for mysite project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gzx%q&33k#_ue(9ouf_0z$$aiv25uom%zgr^_e3hbl6a8nl&^5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["amiraliarzande.ir", "www.amiraliarzande.ir"]

SITE_ID = 2 # Set the site ID for the site framework

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static/'  # Directory for custom static files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for media files
STATICFILES_DIRS = [
    BASE_DIR / 'statics/',  # Additional directory for static files
]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l1*hfpkgbv4$um#oj#pbmm0@5*glvj%j*b5lev)hz&7%t_2uny'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogitdb8',
        'USER': 'blogituser1',
        'PASSWORD': 'blogituser1',
        'HOST': '127.0.0.1',    
        'PORT': '5432',
    }
}
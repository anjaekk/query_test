DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'querytest',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

SECRET_KEY   = 'django-insecure-sv#6-&c3_93h9453yn$mky%v6nfc+@ygvmm9yixymnudfxiw@b'
ALGORITHMS   = 'HS256'
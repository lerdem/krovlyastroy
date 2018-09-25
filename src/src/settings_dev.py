DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "dev",
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '0.0.0.0',
        'PORT': 3306
    }
}

CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
)
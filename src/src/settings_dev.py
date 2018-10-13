DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "dev",
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '0.0.0.0',
        'PORT': 53306
    }
}

# https://github.com/ottoyiu/django-cors-headers/#cors_origin_whitelist
CORS_ORIGIN_WHITELIST = (
    'localhost:63342',
)

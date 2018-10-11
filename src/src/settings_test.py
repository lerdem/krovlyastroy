DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev',
        'USER': 'root',
        'PASSWORD': '',  # according travis docs
        'HOST': '127.0.0.0',
        'PORT': 3306
    }
}

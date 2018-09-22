from django.urls import path

from .views import *

urlpatterns = [
    path(r'hello/', hello, name='hello'),
]
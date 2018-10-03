from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'common-info', CommonInfoViewSet, base_name='common-info')

urlpatterns = [
    path(r'hello/', hello, name='hello'),
    path('', include(router.urls)),
]

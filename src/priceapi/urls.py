from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import CommonInfoViewSet, hello


router = routers.DefaultRouter()
router.register('common-info', CommonInfoViewSet, base_name='common-info')

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', include(router.urls)),
]

from django.urls import path, re_path
from django.conf.urls import url, include

from rest_framework import routers

from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'common-info', CommonInfoViewSet)

urlpatterns = [
    path(r'hello/', hello, name='hello'),
    re_path(r'^', include(router.urls)),
]

#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
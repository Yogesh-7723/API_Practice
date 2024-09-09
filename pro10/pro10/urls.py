from django.contrib import admin
from django.urls import path,include
from api.views import SingerView,SongView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('singerapi',SingerView)
router.register('songapi',SongView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]

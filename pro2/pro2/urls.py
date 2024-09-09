from django.contrib import admin
from django.urls import path,include
from api.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('studentapi',StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]

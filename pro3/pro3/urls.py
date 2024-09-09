from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView
from django.contrib import admin
from rest_framework import routers
from api.views import StudentViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register('studentapi',StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('verifytoken/',TokenVerifyView.as_view(),name='verify_token'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_token')

]

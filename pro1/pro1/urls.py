from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import StudentViewSet
from api.auth import CustomAuth
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = routers.DefaultRouter()
router.register('studentapi',StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('gettoken/',CustomAuth.as_view()),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh_pair'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')

]

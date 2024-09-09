from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    # path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token_refreh'),
    path('auth/',include('rest_framework.urls'))
]

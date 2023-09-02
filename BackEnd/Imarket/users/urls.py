from django.urls import path

from .views import CustomTokenObtainPairView
from .views import send_to_email, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/verify/', send_to_email, name='sending to email'),
    path('register/', RegisterView.as_view(), name='register to the system'),

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
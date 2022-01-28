from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import ArnaTokenObtainPairView, RegisterView


urlpatterns = [
    path('account/login/', ArnaTokenObtainPairView.as_view(), name="login"),
    path('account/refresh/', TokenRefreshView.as_view(), name="refesh"),
    path('account/register/', RegisterView.as_view(), name="register"),
]
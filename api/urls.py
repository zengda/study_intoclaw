from django.urls import path
from .views import RegisterView, LoginView, UserInfoView, RefreshTokenView, LogoutView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/refresh/", RefreshTokenView.as_view(), name="refresh"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("user/info/", UserInfoView.as_view(), name="user-info"),
]
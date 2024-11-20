from django.urls import path

from accounts.views import UserRegisterView, VerifyEmailView, LoginUserView, TestAuthenticationView, \
    PasswordResetConfirmView, PasswordResetRequestView, SetNewPasswordView, LogoutUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', TestAuthenticationView.as_view(), name='profile'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-password'),
]
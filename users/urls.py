from django.urls import path
from .views import RegisterView, ConfirmView, LoginView
from users.google_oauth import GoogleLoginAPIView
from .views import SendConfirmationCodeView, ConfirmView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("confirm/", ConfirmView.as_view()),
    path("login/", LoginView.as_view()),
    path("google-oauth/", GoogleLoginAPIView.as_view()),
    path('send_code/', SendConfirmationCodeView.as_view(), name='send_confirmation_code'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
]
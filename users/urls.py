from django.urls import path
from .views import RegisterView, ConfirmView, LoginView
from users.google_oauth import GoogleLoginAPIView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("confirm/", ConfirmView.as_view()),
    path("login/", LoginView.as_view()),
    path("google-oauth/", GoogleLoginAPIView.as_view()),
]
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, ConfirmSerializer, LoginSerializer
from .models import ConfirmationCode
from users.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from confirmation.utils import save_confirmation_code, check_and_delete_confirmation_code
import random
from users.tasks import add        





class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Регистрация
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()



class ConfirmView(generics.CreateAPIView):
    serializer_class = ConfirmSerializer

    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"]
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "Log in!"}, status=status.HTTP_401_UNAUTHORIZED)

        # Проверяем код в Redis
        if check_and_delete_confirmation_code(user.id, code):
            user.is_active = True
            user.save()
            return Response({"message": "Account has been successfully verified!"}, status=200)
        else:
            return Response({"error": "Invalid or expired code"}, status=400)



class LoginView(APIView):
    def post(self, request):
        add.delay(2,5)  # Пример вызова задачи Celery для сложения чисел    ssddsdd
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )

        if not user:
            return Response({"error": "Incorrect data"}, status=400)
        if not user.is_active:
            return Response({"error": "The account is not activated"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    

class SendConfirmationCodeView(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "Log in!"}, status=status.HTTP_401_UNAUTHORIZED)

        code = f"{random.randint(100000, 999999)}" 
        save_confirmation_code(user.id, code) 

        print(f"Users's confirmation code {user.email}: {code}")

        return Response({"message": "The code has been sent"}, status=status.HTTP_200_OK)
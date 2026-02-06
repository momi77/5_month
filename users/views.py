from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, ConfirmSerializer, LoginSerializer
from .models import ConfirmationCode
from users.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView

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

        try:
            conf = ConfirmationCode.objects.get(code=code)
        except ConfirmationCode.DoesNotExist:
            return Response({"error": "Invalid code"}, status=400)

        user = conf.user
        user.is_active = True
        user.save()

        conf.delete()

        return Response({"message": "Account verified successfully"}, status=200)



class LoginView(APIView):
    def post(self, request):
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
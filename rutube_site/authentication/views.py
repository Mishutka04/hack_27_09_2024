from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User
from .serializers import UserRegisterSerializer


class RegistrationAPIView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)  # Создание Refesh и Access

            refresh.payload.update({  # Полезная информация в самом токене

                'user_id': user.id,

                'username': user.username

            })

            return Response({

                'refresh': str(refresh),

                'access': str(refresh.access_token),  # Отправка на клиент

            }, status=status.HTTP_201_CREATED)
        return Response({
            "error - not form"
        }, status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not (user.password == password):
            raise AuthenticationFailed('Incorrect password!')

        refresh = RefreshToken.for_user(user)

        refresh.payload.update({

            'user_id': user.id,

            'username': user.username

        })
        print(refresh)
        return Response({

            'refresh': str(refresh),

            'access': str(refresh.access_token),

        }, status=status.HTTP_200_OK)
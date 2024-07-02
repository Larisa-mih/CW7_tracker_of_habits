from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.permissions import IsOwner
from users.serializer import CreateUserSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    """Эндпоинт для регистрации"""

    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    """Эндпоинт для вывода списка пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveView(generics.RetrieveAPIView):
    """Эндпоинт для просмотра одного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]


class UserUpdateView(generics.UpdateAPIView):
    """Эндпоинт для обновления или изменения пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]


class UserDestroyView(generics.DestroyAPIView):
    """Эндпоинт для удаления пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]

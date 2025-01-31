from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from habits.models import Habits
from habits.pagination import HabitPagination
from habits.serializer import HabitsSerializer
from habits.tasks import send_notification
from users.permissions import IsOwner


class HabitCreateView(generics.CreateAPIView):
    """Эндпоинт для создания привычки"""

    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        send_notification()


class HabitListView(generics.ListAPIView):
    """Эндпоинт для вывода списка привычек"""

    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habits.objects.filter(owner=user)
        else:
            queryset = Habits.objects.all()
        return queryset


class PublicHabitListView(generics.ListAPIView):
    """Эндпоинт для вывода списка публичных привычек"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination


class HabitRetrieveVIew(generics.RetrieveAPIView):
    """Эндпоинт для просмотра одной привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class HabitUpdateView(generics.UpdateAPIView):
    """Эндпоинт для обновления или изменения привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    """Эндпоинт для удаления привычки"""

    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]

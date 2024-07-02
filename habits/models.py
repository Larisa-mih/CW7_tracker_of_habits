from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
    )
    place = models.CharField(
        max_length=200, verbose_name="Место, где необходимо выполнять привычку"
    )
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время, когда необходимо выполнять привычку",
    )
    action = models.CharField(max_length=300, verbose_name="Привычка")
    is_pleasant_habit = models.BooleanField(
        default=True, **NULLABLE, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    periodicity = models.IntegerField(
        default=1, verbose_name="Периодичность выполнения привычки в неделю"
    )
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name="Вознаграждение")
    time_to_complete = models.IntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите адрес электронной почты"
    )
    phone = models.CharField(max_length=30, **NULLABLE, verbose_name="Телефон")
    city = models.CharField(max_length=50, **NULLABLE, verbose_name="Город")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="Аватар")
    chat_id = models.CharField(max_length=80, **NULLABLE, verbose_name="Телеграм ID")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

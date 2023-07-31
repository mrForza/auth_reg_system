from django.db import models
from django.contrib.auth.models import AbstractUser


HELP_TEXT = {
    'username': 'Придумайте уникальный никнейм',
    'password': 'Пароль должен содержать \n1) цифры \n2) строчные буквы'
                '\n3) заглавные буквы \n4) спецсимволы: + _ ! @ # $ % ^ & *',
    'bio': 'Подробно опишите свой опыт работы'
}


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        help_text=HELP_TEXT['username'],
        unique=True,
        max_length=64
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=128
    )
    password = models.CharField(
        verbose_name='Пароль',
        help_text=HELP_TEXT['password'],
        max_length=128,     
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=64,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=64,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        help_text=HELP_TEXT['bio'],
        max_length=512,
        blank=True
    )
    role = models.CharField(
        verbose_name='Тип аккаунта',
        max_length=12,
        default='user'
    )

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи',
        default_related_name = 'users'
from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    """Задачи"""

    I = 'Важно'
    N = 'Нормально'
    U = 'Неважно'

    PRIORITY_CHOICES = [
        (I, 'Важно'),
        (N, 'Нормально'),
        (U, 'Неважно')
    ]

    C = 'Завершено'
    P = 'В процессе'
    F = 'Заброшено'

    COMPLETION_CHOICES = [
        (C, 'Завершено'),
        (P, 'В процессе'),
        (F, 'Заброшено')
    ]

    class Meta:
        db_table = "tasks"
        verbose_name = "задачу"
        verbose_name_plural = "Задачи"

    title = models.CharField(
        max_length=64,
        default="",
        verbose_name="Название задачи"
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        blank=True,
        null=True
    )
    deadline = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дедлайн"
    )
    priority = models.CharField(
        max_length=len(N),
        choices=PRIORITY_CHOICES,
        blank=True,
        null=True,
        verbose_name="Приоритет"
    )
    employers = models.ManyToManyField(
        User,
        blank=True,
        verbose_name="Сотрудники"
    )
    progress = models.CharField(
        max_length=len(P),
        choices=COMPLETION_CHOICES,
        default=P,
        verbose_name="Состояние"
    )
    expired = models.BooleanField(
        default=False,
        verbose_name="Истек срок исполнения?",
        editable=False
    )

    def __str__(self):
        return f"{self.id} {self.title}"

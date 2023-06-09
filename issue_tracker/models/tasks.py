from django.db import models
from django.utils import timezone

from issue_tracker.managers import CustomManager


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        verbose_name='Краткое описание'
    )

    description = models.TextField(
        null=True, blank=True,
        verbose_name='Полное описание'
    )

    status = models.ForeignKey(
        to='issue_tracker.Status',
        on_delete=models.RESTRICT,
        related_name='tasks',
        verbose_name='Статус'
    )

    type = models.ManyToManyField(
        to='issue_tracker.Type',
        related_name='tasks',
        verbose_name='Тип'
    )

    project = models.ForeignKey(
        to='issue_tracker.project',
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Удалено'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время и дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время и дата обновления'
    )

    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    objects = CustomManager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.summary

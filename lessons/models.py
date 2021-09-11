from django.db import models
from teachers.models import Teachers


class Lessons(models.Model):
    name = models.CharField(verbose_name='Название урока', max_length=255)
    teachers = models.ForeignKey(Teachers, verbose_name='Учитель', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Уроки'

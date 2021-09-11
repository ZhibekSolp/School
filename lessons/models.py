from django.db import models


class Lessons(models.Model):
    name = models.CharField(verbose_name='Название урока')

    class Meta:
        verbose_name_plural = 'Уроки'

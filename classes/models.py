from django.db import models
from teachers.models import Teachers


class Classes(models.Model):
    classletter = models.CharField(verbose_name='Буква класса', max_length=255)
    numberofclass = models.IntegerField(verbose_name='Номер класса', unique=True, default=0)
    superviser = models.CharField(verbose_name='Классный руководитель', max_length=255)
    teachers = models.ForeignKey(Teachers, verbose_name='Учитель', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.classletter

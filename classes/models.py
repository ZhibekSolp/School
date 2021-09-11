from django.db import models

import classes
from teachers.models import Teachers


class Classes(models.Model):
    classletter = models.OneToOneField(classes, verbose_name='Буква класса', max_length=255, on_delete=models.CASCADE)
    numberofclass = models.IntegerField(verbose_name='Номер класса', unique=True, default=0, max_length=50)
    superviser = models.OneToOneField(Teachers, verbose_name='Классный руководитель', max_length=255,
                                      on_delete=models.CASCADE)


class Meta:
    verbose_name_plural = 'Классы'

    def __str__(self):
        return self.classletter

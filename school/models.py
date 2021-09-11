from django.db import models
from director.models import Director
from headteacher.models import HeadTeacher
from teachers.models import Teachers
from classes.models import Classes
from pupils.models import Pupils
from lessons.models import Lessons


class School(models.Model):
    title = models.CharField(verbose_name='Школа', max_length=255)
    director = models.ForeignKey(Director, verbose_name='Директор', on_delete=models.CASCADE)
    headteacher = models.ForeignKey(HeadTeacher, verbose_name='Завучи', on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teachers, verbose_name='Учитель', on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, verbose_name='Классы', on_delete=models.CASCADE)
    pupils = models.ForeignKey(Pupils, verbose_name='Ученики', on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lessons, verbose_name='Уроки', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Школа'

    def __str__(self):
        return self.title

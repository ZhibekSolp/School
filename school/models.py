from django.db import models

from classes.models import Classes
from director.models import Director
from headteacher.models import HeadTeacher
from teachers.models import Teachers


class School(models.Model):
    title = models.CharField(verbose_name='Школа', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Школа'


class Director(models.Model):
    title = models.ForeignKey(Director, verbose_name='Директор', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Директор'


class HeadTeacher(models.Model):
    title = models.ForeignKey(HeadTeacher, verbose_name='Завучи', max_length=255, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Завучи'


class Teachers(models.Model):
    title = models.ForeignKey(Teachers, verbose_name='Учителя', max_length=255, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Учителя'


class Classes(models.Model):
    title = models.ForeignKey(Classes, verbose_name='Классы', max_length=255, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Классы'


class Pupils(models.Model):
    title = models.CharField(verbose_name='Ученики', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ученики'


class lessons(models.Model):
    title = models.CharField(verbose_name='Уроки', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Уроки'

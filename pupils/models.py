from django.db import models


class Pupils(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=255)
    clas = models.CharField(verbose_name='Касс', max_length=255)
    number = models.IntegerField(verbose_name='Номер родителей')
    location = models.CharField(verbose_name='Место проживания', max_lengggth=255)
    image = models.ImageField(upload_to='/image/', verbose_name='Фото')

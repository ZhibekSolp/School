from django.db import models

from school.models import Teachers


class Teachers(models.Model):
    title = models.OneToOneField(Teachers, verbose_name='Учителя', related_name='Учителя', on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name='ФИО', max_length=255)
    address = models.CharField(verbose_name='Место проживания', max_length=255)
    phone = models.CharField(verbose_name='Номер телефона', unique=True, max_length=100)
    photo = models.ImageField(verbose_name='Фото директора', blank=True)


class Meta:
    verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.fullname

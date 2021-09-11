from django.db import models


class Teachers(models.Model):
    title = models.CharField(verbose_name='Учителя', max_length=255)
    fullname = models.CharField(verbose_name='ФИО', max_length=255)
    address = models.CharField(verbose_name='Место проживания', max_length=255)
    phone = models.CharField(verbose_name='Номер телефона', unique=True, max_length=255)
    photo = models.ImageField(verbose_name='Фото директора', blank=True)

    class Meta:
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.fullname

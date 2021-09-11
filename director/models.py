from django.db import models



class Director(models.Model):
    fullname = models.CharField(verbose_name='ФИО', max_length=255)
    photo = models.ImageField(verbose_name='Фото директора', blank=True)
    number = models.IntegerField(verbose_name='Номер', default=0)

    class Meta:
        verbose_name_plural = 'Директор'

    def __str__(self):
        return self.fullname

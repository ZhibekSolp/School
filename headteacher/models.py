from django.db import models

from school.models import HeadTeacher


class HeadTeacher(models.Model):
    title = models.OneToOneField(HeadTeacher, verbose_name='Завучи школы №', on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name='ФИО', max_length=255)
    photo = models.ImageField(verbose_name='Фото завуча', blank=True)
    number = models.IntegerField(verbose_name='Номер', default=0)


class Meta:
    verbose_name_plural = 'Завучи'

    def __str__(self):
        return self.fullname

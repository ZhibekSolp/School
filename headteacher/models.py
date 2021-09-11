from django.db import models


class HeadTeachers(models.Model):
    title = models.CharField(verbose_name='Завучи', max_length=255)


    class Meta:
        verbose_name_plural = 'Завучи'

    def __str__(self):
        return self.title


class HeadTeacher(models.Model):
    fullname = models.CharField(verbose_name='ФИО', max_length=255)
    photo = models.ImageField(verbose_name='Фото завуча', blank=True)
    number = models.IntegerField(verbose_name='Номер', default=0)


    class Meta:
        verbose_name_plural = 'Завучи'


    def __str__(self):
        return self.title

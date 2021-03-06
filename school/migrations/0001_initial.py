# Generated by Django 3.2.7 on 2021-09-11 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('headteacher', '0001_initial'),
        ('pupils', '0001_initial'),
        ('director', '0001_initial'),
        ('classes', '0001_initial'),
        ('lessons', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Школа')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes', verbose_name='Классы')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.director', verbose_name='Директор')),
                ('headteacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='headteacher.headteacher', verbose_name='Завучи')),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lessons', verbose_name='Уроки')),
                ('pupils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pupils.pupils', verbose_name='Ученики')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers', verbose_name='Учитель')),
            ],
            options={
                'verbose_name_plural': 'Школа',
            },
        ),
    ]

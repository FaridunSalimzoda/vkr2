# Generated by Django 3.1.5 on 2021-05-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_patronymic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активированная'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_students',
            field=models.BooleanField(default=True, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(default='lastname', max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(default='name', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.TextField(default='patronymic', max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='students_groups',
            field=models.TextField(default='group', max_length=10, verbose_name='Группа'),
        ),
    ]

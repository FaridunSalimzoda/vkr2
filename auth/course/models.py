from urllib import request
from django.db import models
from users.models import user


User_table = user

class CourseTable(models.Model):
    title = models.CharField('Название курса', max_length=75)
    task = models.TextField('Описание курса', max_length=250)
    teacher = models.ForeignKey(User_table, on_delete=models.CASCADE)


    def get_users(self):
        return "\n".join([u.username for u in self.users.all()])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/course/{self.id}'

    class Meta:

        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class TopicTable(models.Model):
    title = models.CharField('Название темы', max_length=75)
    task = models.TextField('Описание темы', max_length=250)
    id_course = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    def __str__(self):
        return f'Тема {self.title} курса {self.id_course}'

    def get_absolute_url(self):
        return f'/course/{self.id_course.id}/{self.id}'

    class Meta:

        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'

class AssignedCoursesTable (models.Model):
    id_course = models.ForeignKey(CourseTable, on_delete=models.CASCADE)
    # id_user = models.ForeingKe(, on_delete=models.CASCADE)
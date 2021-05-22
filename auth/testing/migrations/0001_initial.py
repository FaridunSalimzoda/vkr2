# Generated by Django 3.2 on 2021-05-22 12:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import testing.models
import testing.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figure', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Файл')),
                ('content', models.CharField(help_text='Введите текст вопроса, который вы хотите показать', max_length=1000, verbose_name='Вопрос')),
                ('explanation', models.TextField(blank=True, help_text='Объяснение должно быть показано после того, как был дан ответ на вопрос.', max_length=2000, verbose_name='Объяснение')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.coursetable', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='a description of the quiz', verbose_name='Описание')),
                ('url', models.SlugField(help_text='Введите ссылку', max_length=60, verbose_name='Ссылка теста')),
                ('random_order', models.BooleanField(default=False, verbose_name='Перемешать вопросы')),
                ('max_questions', models.PositiveIntegerField(blank=True, help_text='Количество вопросов, на которые ужно ответить при каждой попытке.', null=True, verbose_name='Количество вопросов')),
                ('answers_at_end', models.BooleanField(default=False, help_text='Правильный ответ не отображается после вопроса. Ответы отображаются в конце.', verbose_name='Ответы отображаются в конце')),
                ('exam_paper', models.BooleanField(default=False, help_text='Если да, то результат каждой попытки пользователя будет сохранен. Необходимо для маркировки.', verbose_name='Экзамен')),
                ('single_attempt', models.BooleanField(default=False, help_text='Если включенно, то можно пройти только одну попытку', verbose_name='Одна попытка')),
                ('pass_mark', models.SmallIntegerField(blank=True, default=0, help_text='Процент для минимального прохождения теста.', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Минимальный процент')),
                ('success_text', models.TextField(blank=True, help_text='При неправельном прохождение теста', verbose_name='Отображается, если пользователь проходит тест')),
                ('fail_text', models.TextField(blank=True, help_text='Отображается, если пользовательне проходит тест.', verbose_name='При неправельном прохождение теста')),
                ('draft', models.BooleanField(blank=True, default=False, help_text='Если да, то тест не отображаетсяв списке викторин и может быть тольковзято пользователями, которые могут редактировать тест.', verbose_name='Проект')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.topictable', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='MCQQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testing.question')),
                ('answer_order', models.CharField(blank=True, choices=[('content', 'Content'), ('none', 'None')], help_text='Порядок, в котором множественном варианты ответа отображаются для пользователя', max_length=30, null=True, verbose_name='Порядок ответа')),
            ],
            options={
                'verbose_name': 'Вопрос С множественным Выбором',
                'verbose_name_plural': 'Вопросы С множественным Выбором',
            },
            bases=('testing.question',),
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_order', models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question Order')),
                ('question_list', models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Question List')),
                ('incorrect_questions', models.CharField(blank=True, max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Incorrect questions')),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
                ('user_answers', models.TextField(blank=True, default='{}', verbose_name='User Answers')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.quiz', verbose_name='Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'permissions': (('view_sittings', 'Can see completed exams.'),),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(blank=True, null=True, to='testing.Quiz', verbose_name='Вопрос'),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Счет')),
                ('correct_answer', models.CharField(max_length=10, verbose_name='Правельные ответы')),
                ('wrong_answer', models.CharField(max_length=10, verbose_name='Неправельные ответы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='CSVUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('file', models.FileField(upload_to=testing.models.upload_csv_file, validators=[testing.validators.csv_file_validator])),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Введите текст ответа, который                                             вы хотите показать', max_length=1000, verbose_name='Содержание')),
                ('correct', models.BooleanField(default=False, help_text='Это правильный ответ?', verbose_name='Правильный')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.mcqquestion', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]

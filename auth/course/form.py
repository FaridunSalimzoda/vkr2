from .models import CourseTable,TopicTable
from django.forms import ModelForm, TextInput, Textarea, Select


class CourseTableForm(ModelForm):
    class Meta:
        model = CourseTable
        fields = ['title', 'task', 'teacher']

        widgets = {
            'title': TextInput(attrs={
                'class': '',
                'placeholder': 'Название курса'
            }),
            'task': Textarea(attrs={
                'class': '',
                'placeholder': 'Описание курса'
            }),
            'teacher': Select(attrs={
               'class': '',
               'placeholder': 'Преподаватель'
           })
        }


class topicform(ModelForm):
    class Meta:
        model = TopicTable
        fields = ['title', 'task', 'id_course']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                'placeholder': 'Название темы'
            }),
            'task': Textarea(attrs={
                'class': 'form_class',
                'placeholder': 'Описание темы'
            }),
            'id_course': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Название курса'
            }),
        }

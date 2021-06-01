from django import forms
from django.forms.widgets import RadioSelect
from django.forms import ModelForm, TextInput, Textarea, Select, CharField, CheckboxInput, ImageField, PasswordInput
from  .models import Quiz
from quiz.models import Question
from mcq.models import MCQQuestion
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from django.contrib.admin.widgets import FilteredSelectMultiple

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'random_order', 'max_questions', 'answers_at_end',
                  'exam_paper', 'pass_mark','single_attempt', 'fail_text', 'draft', 'success_text', 'url']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_class',
                }),
            'description': Textarea(attrs={
                'class': 'form_class',

            }),
            'category': Select(attrs={
                'class': 'form_class',

            }),
               'random_order': CheckboxInput(attrs={

               }),

                  'max_questions': TextInput(attrs={
                      'class': 'form_class'
                  }),
                  'answers_at_end': CheckboxInput(attrs={}),
                'exam_paper': CheckboxInput(attrs={}),
                  'single_attempt': CheckboxInput(attrs={
                      'class': 'form_class',
                      'placeholder': 'Пользователю будет разрешена только одна попытка'
                  }),
                  'pass_mark': TextInput(attrs={}),
                'success_text': TextInput(attrs={'class': 'form_class'}),
                'fail_text': TextInput(attrs={'class': 'form_class'}),
                'draft': CheckboxInput(attrs={}),
                'url': TextInput(attrs={})
        }

class  QuestionsFormmy(ModelForm):
    class Meta:
        model = MCQQuestion
        fields = ['category', 'content', 'explanation']
        widgets = {
            # здесь может быть поле для выбора теста, в который должен попавсть вопрос
            # 'quiz': TextInput(attrs={
            #     'class': 'form_class'
            # }),

            'category': Select(attrs={
                'class': 'form_class',
                'placeholder': 'Курс'
            }),


            'content': TextInput(attrs={
                'class': 'form_class'
            }),

            'explanation': TextInput(attrs={
                'class': 'form_class',

            }),

        }

class RegistrForm(ModelForm):
    class Meta:
        model: User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput({}),
            'password': PasswordInput({})
        }
# class MCQQuestForm(ModelForm):
#     class Meta:
#         model =
#         fields = ['answer_order', 'check_if_correct', 'order_answers', 'get_answers', 'get_answers_list', 'answer_choice_to_string']
#         widgets = {
#             'answer_order': Select({}),
#             'check_if_correct': CheckboxInput({}),
#             'order_answers': CheckboxInput({}),
#             'get_answes': CheckboxInput({}),
#             'get_answers_list': CheckboxInput({}),
#             'answer_choice_to_string': CheckboxInput({})
#
#
#         }
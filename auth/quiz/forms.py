from django import forms
from django.forms.widgets import RadioSelect
from django.forms import ModelForm, TextInput, Textarea, Select, CharField, CheckboxInput, ImageField, PasswordInput, FileInput
from .models import Quiz
from quiz.models import Question
from mcq.models import MCQQuestion, Answer
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class QuizForm(ModelForm):
    class Meta:
        model = Quiz

        fields = ['title', 'description', 'category', 'random_order', 'max_questions', 'answers_at_end',
                  'exam_paper', 'pass_mark', 'single_attempt', 'fail_text', 'draft', 'success_text', 'url']
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
            'url': TextInput(attrs={}),

        }

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Вопросы"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Вопросы"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()
            print(self.fields)

    def save(self, commit=True):
        quiz = super(QuizForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'correct']
        widgets = {
            'content': Select(attrs={}),
            'correct': CheckboxInput
        }

class QuestionsFormmy(ModelForm):
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
                'placeholder': 'Тема'
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

from django.core.exceptions import ValidationError

from .models import user
from django.forms import  ModelForm, TextInput, PasswordInput, ImageField, CharField

class UserRegisterForm(ModelForm):
    password = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Повторите пароль', widget=PasswordInput)
    class Meta:
        model = user
        fields = ['email','name','last_name', 'patronymic']

        widgets ={
            'email': TextInput(attrs={

        }),

            'name': TextInput(attrs={}),
            'last_name': TextInput(attrs={}),
            'patronymic': TextInput(attrs={})

        }

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise ValidationError('Пароли не совпадают!')
            return cd['password2']
class UserUpdateForm(ModelForm):
    class Meta:
        model = user
        fields = ['password', 'photo']

        widgets = {
            'password': PasswordInput(attrs={
                'class':'',
                'placeholder': 'Введите пароль'
            }),
            # 'photo': ImageField

        }
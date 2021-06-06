from .models import user
from django.forms import  ModelForm, TextInput, PasswordInput, ImageField


class UserUpdateForm(ModelForm):
    class Meta:
        model = user
        fields = ['password', 'photo']

        widgets = {
            'password': PasswordInput(attrs={
                'class':'',
                'placeholder': 'Введите пароль'
            }),
            'photo': ImageField

        }
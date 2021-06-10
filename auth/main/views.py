import random

from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
#from .forms import QuestionForm, QuizForm, QuestionsFormmy, RegistrForm
#from .models import Quiz, Category, Progress, Sitting, Question
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm
from django.views.generic import UpdateView, DeleteView
from users.models import user
from users.forms import UserRegisterForm
User_table = user

def index(request):

    return render(request, 'main/index.html')
@login_required
def account(request):

    return render(request, 'main/account.html')
def teacher(request):

    return render(request, 'main/teacher.html')

def students(request):
    # можно вывести только студентов:
    u = user.objects.filter(is_students=True)
    return render(request, 'main/students.html', {'u':u})

def user_all(request):
    # можно просто вывести всех:
    # u = user.objects.all()
    # можно отсортировать
    u = user.objects.order_by('name')
    return render(request, 'main/user.html', {'u':u})
def user_detail(request, pk):
    a = list(user.objects.filter(id=pk).values())
    return  render(request, 'main/user_detail.html', {'a':a})
@login_required
def my_view(request):
    if not request.user.is_authenticated():
        return render(request, 'myapp/error_403.html')

class setting_user(UpdateView):
    model = user
    template_name = 'main/setting_user.html'
    form_class =UserUpdateForm

# def setting_user(request, ):
#     return render(request, 'main/setting_user.html')

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have successfully logged in')
#             return redirect("ho")
#         else:
#             messages.success(request, 'Error logging in')
#             return redirect('login')
#     else:
#         return render(request, 'main/login.html', {})

def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            if user.is_admin:
                return redirect("ho")
            if user.is_teacher:
                return redirect("teacher")
            if user.is_students:
                return redirect("students")
        else:
            error='Не правильный логин или пароль'
            return render(request, "main/login.html", {'error':error})
    else:
     return render(request, 'main/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    print('logout function working')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/login.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'main/register.html', {'user_form': user_form})
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
User_table = user

def index(request):

    return render(request, 'main/index.html')
@login_required
def account(request):

    return render(request, 'main/account.html')
def teacher(request):

    return render(request, 'main/teacher.html')

def students(request):

    return render(request, 'main/students.html')
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
            return render(request, "main/login.html")
    else:
     return render(request, 'main/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    print('logout function working')
    return redirect('login')

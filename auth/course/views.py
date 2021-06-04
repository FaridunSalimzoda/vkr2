from django.shortcuts import render, redirect
from .models import CourseTable, TopicTable
from .form import CourseTableForm, topicform, AssignedCoursesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib import auth


def cour(request):
    ku = CourseTable.objects.order_by('id')
    return render(request, 'cours/cours_home.html', {'ku': ku})

def user_cours(request):
    ku = CourseTable.objects.order_by('id')
    return render(request, 'cours/user_cours.html', {'ku': ku})

def detail(request, pk):
    ku = list(CourseTable.objects.filter(id=pk).values())
    top = TopicTable.objects.filter(id_course=pk)
    user = auth.get_user(request)
    return render(request, 'cours/datail.html', {'post': ku[0], 'top': top, 'pk': pk, 'user':user})

def topic_dateil(request, pk, kk):
    top = TopicTable.objects.filter(id_course=pk)
    ku = list(CourseTable.objects.filter(id=pk).values())
    return render(request, 'cours/topic.html', {'top': top[0], 'pk': pk, 'kk': kk})

def my_cours(request):
    ku = CourseTable.objects.order_by('teacher')
    return render(request, 'cours/mykurs.html', {'ku': ku})



class kursUpdateView(UpdateView):
    model = CourseTable
    template_name = 'cours/update.html'

    form_class = CourseTableForm

class topicUpdateView(UpdateView):
    model = TopicTable
    template_name = 'cours/update_topic.html'

    form_class = topicform

class kursDeleteView(DeleteView):
    model = CourseTable
    success_url = '/course/'
    template_name = 'cours/cours_delete.html'

class topicDeleteView(DeleteView):
    model = TopicTable
    success_url = '/course/'
    template_name = 'cours/delete_topic.html'


def newtopic(request, pk: any):
    error = ''
    if request.method == 'POST':
        form = topicform(request.POST)
        if form.is_valid():
            # form['kursu'] = kursu.objects.filter(id=pk)
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
    form = topicform()
    # form['kursu'] = kursu.objects.filter(id=pk)
    data = {
        'form': form,
        'error': error,
        'pk': pk
    }
    return render(request, 'cours/addTopic.html', data)

def adk(request):
    error = ''
    if request.method == 'POST':
        form = CourseTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
    form = CourseTableForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cours/addKurs.html', data)

def record(request):
    error = ''
    if request.method == 'POST':
        form = AssignedCoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kurs')
        else:
            error = 'error'
            form = AssignedCoursesForm()
            date = {
                'form': form,
                'error': error
            }
            return render(request, 'cours/RecordToCourse.html', date)
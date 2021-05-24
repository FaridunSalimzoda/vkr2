from django.conf.urls import url
from django.urls import path
from .views import QuizListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake
from  . import views
from django.urls import path


urlpatterns = [           path('adt', views.add_test, name='add_test'),
                          path('add', views.add_questions, name='add_answer'),
                          path('registr', views.add_user, name='add_user'),
                          url(regex=r'^quizzes/$', view=QuizListView.as_view(),name='quiz_index'),

                          url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$', view=ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
                          url(regex=r'^progress/$', view=QuizUserProgressView.as_view(), name='quiz_progress'),
                          url(regex=r'^marking/$', view=QuizMarkingList.as_view(), name='quiz_marking'),
                          url(regex=r'^marking/(?P<pk>[\d.]+)/$', view=QuizMarkingDetail.as_view(),name='quiz_marking_detail'),
                       #  passes variable 'quiz_name' to quiz_take view
                          url(regex=r'^(?P<slug>[\w-]+)/$', view=QuizDetailView.as_view(), name='quiz_start_page'),
                          url(regex=r'^(?P<quiz_name>[\w-]+)/take/$', view=QuizTake.as_view(),                     name='quiz_question'),

]
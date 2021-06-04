from django.urls import path, include
from . import views


urlpatterns = [

        path('test/', include('quiz.urls'), name='add_test'),
        path('', views.cour, name='kurs'),
        path('user_course', views.user_cours, name = 'user_course'),
        path('adk', views.adk, name='adk'),
        path('record', views.record, name='record'),
        path('mycours', views.my_cours, name='mycours'),
        path('<int:pk>/', views.detail, name='datail'),
        path('<int:pk>/new_topic', views.newtopic, name='newtopic'),
        path('<int:pk>/update', views.kursUpdateView.as_view(), name='update'),
        path('<int:pk>/delete', views.kursDeleteView.as_view(), name='delete'),
        path('<int:pk>/<int:kk>', views.topic_dateil, name='top_datail'),
        path('<int:pk>/<int:kk>/delete_topic', views.topicDeleteView.as_view(), name='topic_delete'),
        path('<int:pk>/<int:kk>/update_topic', views.topicUpdateView.as_view(), name='topic_update')
    ]
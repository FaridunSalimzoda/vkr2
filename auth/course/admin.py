from django.contrib import admin
from .models import CourseTable, TopicTable

class adminCoursTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'teacher')
    list_filter =('title', 'task', 'teacher')

class adminTopicTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'id_course')

admin.site.register(CourseTable, adminCoursTable),
admin.site.register(TopicTable, adminTopicTable),

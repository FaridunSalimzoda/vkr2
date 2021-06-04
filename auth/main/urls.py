from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import index, login_user, logout_user, account, setting_user
urlpatterns = [
    url(regex=r'^$', view=index, name='ho'),
    url(regex=r'^account', view=account, name='account'),
    url(regex=r'^login/$', view=login_user, name='login'),
    url(regex=r'^logout/$', view=logout_user, name='logout'),
    url(regex=r'^settings/$', view=setting_user, name='setting')
    ]
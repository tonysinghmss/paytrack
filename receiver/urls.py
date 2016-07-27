'''
Created on Jul 27, 2016

@author: TONY
'''
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

'''
Created on Apr 10, 2016

@author: lieyongzou
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_global),
    url(r'^index/global.html$', views.index_global, name = 'global'),
    url(r'^index/mypost.html$', views.index_mypost, name = 'mypost'),
    url(r'^index/register/(?P<username>\w+)$', views.onRegister, name = 'register'),
    url(r'^index/writePost/$', views.writePost, name = 'writePost'),
]
from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [

    path('', blog_home, name='blog_home'),
    path('<int:pid>', blog_single, name='blog_single'),
    path('test/', test, name='test')
   
]
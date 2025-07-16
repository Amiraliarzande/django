from django.contrib import admin
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact , name='contact'),
    path('elements/', elements, name='elements'),
]
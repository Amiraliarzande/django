from django.urls import path
from website.views import *

urlpatterns = [
    path('', home),
    path('about', about),
    path('contact', contact),
    path('elements', elements)
]
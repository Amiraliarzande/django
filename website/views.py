from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse , JsonResponse
def home(request):
    return HttpResponse("<h1>home</h1>")
def about(request):
    return HttpResponse("<h1>about</h1>")



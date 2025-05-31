from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse , JsonResponse

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')



from django.shortcuts import render
from django.http import HttpResponse

def maintenance(request):
    return render(request, 'maintenance.html')
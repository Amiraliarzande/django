from django.shortcuts import render
from blog.forms import Contactform , newsletterform
from django.contrib import messages


# Create your views here.

from django.http import HttpResponse , JsonResponse ,HttpResponseRedirect

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact (request):

    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The operation has been performed correctly.")
        else:
            messages.error(request, "The operation was not performed correctly.")

            
        
    form = Contactform()
    return render(request, "website/contact.html",{"form": form})

def elements(request):
    return render(request, 'website/elements.html')

def newsletter (request):

    if request.method == "POST":
        form = newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    else:
        return HttpResponseRedirect('/')
    return render(request, "base.html",{"form": form})




from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import logout
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.urls import is_valid_path

# Create your views here.

def login_view(request):
    
    next_url = request.GET.get('next', '/')

    if not request.user.is_authenticated:
    
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            next_url = request.POST.get('next', '/')
            print("Next URL:", next_url)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful.")

                    return redirect(next_url)
        else:
            form = AuthenticationForm()  

                
        form = AuthenticationForm()
        context = {
            'form': form,
            'next': next_url
        }
        return render(request, 'account/login.html', context)
    
    else:
        return redirect('/')
        

def logout_view(request):
    
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out.")
    return redirect('/')

def signup_view(request):

    next_url = request.GET.get('next', '/')

    if not request.user.is_authenticated:
        if request.method == "POST" :
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully.")

                next_url = request.POST.get('next', next_url)
                parsed_url = urlparse(next_url)
                if not parsed_url.netloc and is_valid_path(next_url):
                    return redirect(next_url)

                return redirect('/')
            else:
                messages.error(request, "Account creation failed.")
                
        form = UserCreationForm()
        context = {
            'form': form,
            'next': next_url
        }
        return render(request, 'account/signup.html', context)
    else:

        return redirect('/')

            
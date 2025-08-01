from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import logout
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from accounts.forms import CustomLoginForm

# Create your views here.

def login_view(request):
    
    next_url = request.GET.get('next', '/')

    if not request.user.is_authenticated:
    
        if request.method == "POST":
            form = CustomLoginForm(request.POST)
            next_url = request.POST.get('next', '/')
            if form.is_valid():
                identifier = form.cleaned_data.get('identifier')
                password = form.cleaned_data.get('password')

                try:
                    user_obj = User.objects.get(email=identifier)
                    username = user_obj.username
                    
                except User.DoesNotExist:
                    username = identifier

                except User.MultipleObjectsReturned:
                    messages.error(request, "Multiple users found with this email. Use your username instead.")
                    return render(request, 'account/login.html', {'form': form, 'next': next_url})

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
            form = RegistrationForm(request.POST)
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

        form = RegistrationForm()
        context = {
            'form': form,
            'next': next_url
        }
        return render(request, 'account/signup.html', context)
    else:

        return redirect('/')

            
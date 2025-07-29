from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import logout


# Create your views here.

def login_view(request):
            
    if not request.user.is_authenticated:
    
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful.")
                    return redirect('/')
            
                
        form = AuthenticationForm()
        context = {
            'form': form
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

    if not request.user.is_authenticated:
        if request.method == "POST" :
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully.")
                return redirect('/')
            else:
                messages.error(request, "Account creation failed.")
        form = UserCreationForm()
        context = {
        'form': form
        }
        return render(request, 'account/signup.html', context)
    else:

        return redirect('/')

            
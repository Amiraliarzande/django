from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/')
    return render(request, 'account/login.html')

# def logout_view(request):
    # Logic for handling logout

def signup_view(request):
    # Logic for handling signup
    return render(request, 'account/signup.html')
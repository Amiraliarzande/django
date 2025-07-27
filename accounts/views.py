from django.shortcuts import render

# Create your views here.

def login_view(request):
    # Logic for handling login
    return render(request, 'account/login.html')

# def logout_view(request):
    # Logic for handling logout

def signup_view(request):
    # Logic for handling signup
    return render(request, 'account/signup.html')
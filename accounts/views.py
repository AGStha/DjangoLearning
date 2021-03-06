from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def login(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')



def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        #REQUEST LOGIC
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

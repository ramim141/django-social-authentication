from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm 
# from social_core.utils import strategy


def home(request):
    return render(request, 'authentication_app/home.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication_app/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                pass
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


# @login_required
# def profile_view(request):
#     return render(request, 'authentication_app/profile.html')



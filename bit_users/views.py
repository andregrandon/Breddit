from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  

# Your view functions here



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page upon successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'bit_users/signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, request.POST)  # Define form outside of the if block
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            form = AuthenticationForm()
            
    return render(request, 'bit_users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')  # Redirect to the home page after logout


class HomePageView(View):
    def get(self, request):
        return render(request, 'bit_users/home.html')


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('bit_posts:post-list-create')) 
    else:
        form = CustomUserCreationForm()
    return render(request, 'bit_users/signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, request.POST)  # Define form outside of the if block
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('bit_posts:post-list-create'))  # Redirect to post listings upon successful login
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


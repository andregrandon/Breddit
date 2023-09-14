# appname/urls.py
from django.urls import path
from . import views

app_name = 'bit_users' 
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),




]

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse


class HomePage(TemplateView):
    template_name = 'home.html'
    
class ContactPage(TemplateView):
    template_name='contact.html'
    
class PrivacyPage(TemplateView):
    template_name='privacy.html'
    
def my_view(request):
    response = render(request, 'home.html')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response


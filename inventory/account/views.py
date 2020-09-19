from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def register(request):
    return render(request, 'account/register.html')
   
       

   


def login(request):
    return render(request, 'account/login.html')

    






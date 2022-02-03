from datetime import datetime
import profile
from urllib import request
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used!')
                return redirect('register')
            else:
                user=User.objects.create(username=email,first_name=username,email=email,password=password)
                user.save()
                auth_token=str(uuid.uuid4())
                profile=Profile.objects.create(user=user,auth_token=auth_token,dated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                profile.save()
                send_email(email,auth_token)
                return redirect('/token/')


        else:
            messages.info(request,'Password did not match, Try Again!')
            return redirect('register')
       
    return render(request,'register.html')


def success(request):
    return render(request,'success.html')

def token_send(request):
    return render(request,'token_send.html')

def welcome(request):
    return render(request,'welcome.html')

def verify(request, auth_token):
    profile_obj=Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'Your Account has been verified')
        return redirect('/')
    else:
        return redirect('/error/')


def send_email(email,token):
    subject='Your account needs to be verified'
    message=f'Click on the given link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)

def error(request):
    return render(request,'error.html')
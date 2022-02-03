from datetime import datetime
import profile
import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

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
                return redirect('/token/')


        else:
            messages.info(request,'Password did not match, Try Again!')
            return redirect('register')
       
    return render(request,'register.html')


def success(request):
    return render(request,'success.html')

def token_send(request):
    return render(request,'token_send.html')
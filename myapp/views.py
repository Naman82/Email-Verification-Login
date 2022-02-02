from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

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
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

        else:
            messages.info(request,'Password did not match, Try Again!')
            return redirect('register')
       
    return render(request,'register.html')


def success(request):
    return render(request,'success.html')
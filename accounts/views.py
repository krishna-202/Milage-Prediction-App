from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
# Create your views here.

def register(request):
    registered=False
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        portfolio=request.POST['portfolio']
        profile_pic=request.FILES['profile_pic']


        user=User()
        user_profile=UserProfile()
        if password1==password2:

            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,"username or email Aleady Exists")
                
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                user_profile.portfolio=portfolio


                user_profile.profile_pic=request.FILES['profile_pic']
                user_profile.user=user
                user_profile.save()
                registered=True
        else:
            messages.info(request,"Password Mismatch!")



    return render(request,'Register.html',{'registered':registered})

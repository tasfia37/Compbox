from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from complain.models import Complain


def signup(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST['nid'] and request.POST['email'] and request.POST['pass']:
            if request.POST['pass']==request.POST['cpass']:
               try:
                   user = User.objects.get(username=request.POST['nid'])
                   return render(request, 'accounts/signup.html', {'error':'This nid has already been used'})
               except User.DoesNotExist:
                   user = User.objects.create_user(request.POST['nid'],email=request.POST['email'],first_name=request.POST['username'], password=request.POST['pass'])
                   auth.login(request,user)
                   return redirect('home')

            else:
                return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'All fields required'})
    else:
        return render(request,'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['nid'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'NID or password or username does not match'})
    else:
        return render(request, 'accounts/login.html')



def mlogin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['ministry'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('mhome')
        else:
            return render(request, 'accounts/mlogin.html', {'error': 'Ministry name or password or username does not match'})
    else:
        return render(request, 'accounts/mlogin.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html')  

    
def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
            except Exception as err:
                return render(request, 'accounts/register.html')
            else:
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/register.html')
    return render(request, 'accounts/register.html') 
    
def logout(request):
    auth.logout(request)
    return redirect('login')
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from accounts.tasks import send_email_reset_password_task
from profiles.models import Profile
import uuid

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back, {}!'.format(user.get_username()))
            return redirect('index')
        else:
            messages.error(request, 'Something is going wrong!')
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
                messages.error(request, 'Invalid data!')
                return render(request, 'accounts/register.html')
            else:
                auth.login(request, user)
                messages.success(request, 'Welcome to BLOGIT APP, {}!'.format(user.get_username()))
                return redirect('index')
        else:
            messages.error(request, 'Passwords did not match!')
            return render(request, 'accounts/register.html')
    return render(request, 'accounts/register.html') 
    
def logout(request):
    auth.logout(request)
    messages.info(request, 'Good bye!')
    return redirect('login')

def forgot_password(request):
    
    if request.user.is_authenticated:
        messages.info(request, 'You are authenticated and can not use forgot passport option')
        return redirect('index')
    
    if request.method == 'GET':
        return render(request, 'accounts/forgot_password.html')
    
    if request.method == 'POST':
        email = request.POST['email']
        # проверим email в базе данных
        try:
            user = User.objects.get(email=email)
        except:
            #если email не нашелся - то сообщение об ошибке
            messages.error(request, 'This email is not register!')
            return render(request, 'accounts/forgot_password.html')
        else:
            profile = Profile.objects.get(user=user)
            #условие если есть, то отправляем ссылку
            link = profile.reset_password_link_uuid
            subject = 'Forgot password [BlogIT]'
            message = f'Click to link to reset password:\n\nhttp://127.0.0.1:8000/accounts/change_password/{link}'
            send_email_reset_password_task.delay(message=message, email=email, subject=subject )
            messages.success(request, 'Email has been sent to address, {}!'.format(email))
            return redirect('forgot_password')
        
def change_password(request, reset_password_link_uuid):
    
    try:
        profile = Profile.objects.get(reset_password_link_uuid=reset_password_link_uuid)
    except:
        messages.error(request, 'somethig going wrong!')
        return render(request, 'accounts/forgot_password.html')
    else:
        user=profile.user

    if request.method == 'GET':
        return render(request, 'accounts/change_password.html')
    
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            user.set_password(password)
            user.save()
            #обновление ссылки на восстановление после смены пароля
            profile.reset_password_link_uuid = uuid.uuid4
            messages.success(request, 'Your password successfully changed!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords did not mach!')
            return render(request, 'accounts/change_password.html')
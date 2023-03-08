from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')  

def login(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')

def register(request):
    return render(request, 'pages/register.html')

def edit(request):
    return render(request, 'pages/edit.html')




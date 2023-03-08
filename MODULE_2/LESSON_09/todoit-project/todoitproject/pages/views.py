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

def examples(request):

    context = { 
        'friends': ['Deadpool', 'Batman', 'Superman'],
        'demo': 'this is a demo',
        'dict_example': {
            'name': 'Nick',
            'lastname': 'Jones',
            'age': 23,
            'hobbies': [
                'programming',
                'hockey',
                'art'
            ]
        }
    }
    return render(request, 'pages/examples.html', context=context)



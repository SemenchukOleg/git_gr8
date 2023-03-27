from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib import messages

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'pages/index.html', context=context)

def create_task(request):
    if request.method == 'POST':
        new_task = Task()
        if 'title' in request.POST:
            new_task.title = request.POST['title']
        if 'description' in request.POST:
            new_task.description = request.POST['description']
        if 'priority' in request.POST:
            new_task.priority = request.POST['priority']
        new_task.save()
        messages.add_message(request, messages.SUCCESS, 'Task #{} successfully created!'.format(new_task.id))
        return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    messages.add_message(request, messages.SUCCESS, 'Task #{} status has been changed!'.format(task_id))
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.add_message(request, messages.WARNING, 'Task #{} is deleted!'.format(task_id))
    return redirect('index')

def complete_all_tasks(request):
    tasks = Task.objects.filter(is_completed=False)
    for task in tasks:
        task.is_completed = True
        task.save()
    messages.add_message(request, messages.SUCCESS, 'All tasks is complited!!!')
    return redirect('index')

def delete_all_complete_tasks(request):
    tasks = Task.objects.filter(is_completed=True)
    for task in tasks:
        task.delete()
    messages.add_message(request, messages.WARNING, 'Complite tasks is deleted!')
    return redirect('index')

def delete_all_tasks(request):
    tasks = Task.objects.filter(is_completed=False)
    for task in tasks:
        task.delete()
    messages.add_message(request, messages.WARNING, 'Delete tasks is deleted!')
    return redirect('index')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {
        'task': task,
    }
    if request.method == 'GET':
        return render(request, 'pages/edit_task.html', context=context)
    if request.method == 'POST':
        if 'title' in request.POST:
            task.title = request.POST['title']
        if 'description' in request.POST:
            task.description = request.POST['description']
        if 'priority' in request.POST:
            task.priority = request.POST['priority']
        task.save()
    messages.add_message(request, messages.SUCCESS, 'Task #{} successfully changed!'.format(task.id))
    
    return redirect('index')
        

'''def index(request):
    return render(request, 'pages/index.html')  

def login(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')

def register(request):
    return render(request, 'pages/register.html')

def edit(request):
    return render(request, 'pages/edit.html')'''




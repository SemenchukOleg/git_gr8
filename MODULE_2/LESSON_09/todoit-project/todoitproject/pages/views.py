from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    context = {
        'tasks' : tasks
    }
    return render(request, 'pages/index.html', context=context)

@login_required
def create_task(request):
    if request.method == 'POST':
        user = request.user
        new_task = Task()
        if 'title' in request.POST:
            new_task.title = request.POST['title']
        if 'description' in request.POST:
            new_task.description = request.POST['description']
        if 'priority' in request.POST:
            new_task.priority = request.POST['priority']
        new_task.user = user    
        new_task.save()
        messages.add_message(request, messages.SUCCESS, 'Task #{} successfully created!'.format(new_task.id))
        return redirect('index')

@login_required
def complete_task(request, task_id):
    user = request.user
    task = Task.objects.get(id=task_id, user=user)
    task.is_completed = not task.is_completed
    task.save()
    if task.is_completed == True:
        messages.add_message(request, messages.SUCCESS, 'Task #{} has been completed!'.format(task_id))
    else :
        messages.add_message(request, messages.WARNING, 'Task #{} status has been changed!'.format(task_id))
    return redirect('index')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id,  user = request.user)
    task.delete()
    messages.add_message(request, messages.WARNING, 'Task #{} is deleted!'.format(task_id))
    return redirect('index')

@login_required
def complete_all_tasks(request):
    user = request.user
    tasks = Task.objects.filter(is_completed=False).filter(user = user)
    for task in tasks:
        task.is_completed = True
        task.save()
    messages.add_message(request, messages.SUCCESS, 'All tasks is complited!!!')
    return redirect('index')

@login_required
def delete_all_complete_tasks(request):
    tasks = Task.objects.filter(is_completed=True,  user = request.user)
    for task in tasks:
        task.delete()
    messages.add_message(request, messages.WARNING, 'Complite tasks is deleted!')
    return redirect('index')

@login_required
def delete_all_tasks(request):
    tasks = Task.objects.filter(is_completed=False,  user = request.user)
    for task in tasks:
        task.delete()
    messages.add_message(request, messages.WARNING, 'Delete tasks is deleted!')
    return redirect('index')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id,  user = request.user)
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

@login_required
def profile(request):
    task = Task.objects.filter(user = request.user)
    context = {
        'active_tasks': task.filter(is_completed=False).count(),
        'completed_tasks' : task.filter(is_completed=True).count(),
    }
    return render(request, 'pages/profile.html', context=context)


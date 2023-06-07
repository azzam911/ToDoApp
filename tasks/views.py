from django.shortcuts import render
from .models import Task
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
# from django.contrib.auth.models import Task

def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Succsufly" )
            return redirect('/')

    return render(request, 'tasks/update_task.html', {'form':form})


def index(request):
    tasks = Task.objects.all()
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks':tasks, 'forms': form, 'count':len(tasks) > 1}
    return render(request, 'tasks/list.html', context)



def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('/')


def deleteAll(request):
    task = Task.objects.all()
    task.delete()
    return redirect('/')
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from To_Do_app.models import ToDo

# Create your views here.

def index(request):
    undone = ToDo.objects.filter(done=False).order_by('-created_at')
    done = ToDo.objects.filter(done=True).order_by('-created_at')
    context = {'undone': undone, 'done': done}
    return render(request,'index.html',context)

def markDone(request,pk):
    task = get_object_or_404(ToDo, pk=pk)
    task.done = True
    task.save()
    return redirect('index')

def markUndone(request,pk):
    task = get_object_or_404(ToDo, pk=pk)
    task.done = False
    task.save()
    return redirect('index')

def deleteTask(reques,pk):
    task = get_object_or_404(ToDo,pk=pk)
    task.delete()
    return redirect('index')

def addTask(request):
    task = request.POST['task']
    if task == '':
        return redirect('index')
    ToDo.objects.create(task=task)
    return redirect('index')

def updateTask(request,pk):
    
    taskToUpdate = request.POST.dict()
    task = get_object_or_404(ToDo, pk=pk)
    new_task = taskToUpdate.get('task','')
    if not new_task.strip():
            new_task = task.task
    task.task = new_task
    if taskToUpdate.get('is_done'):
        task.done = True
    else:
        task.done = False
    task.save()

    return redirect('index')

def editPage(request,pk):
    task = get_object_or_404(ToDo, pk=pk)
    context = {
        'pk':pk,
        'task':task
    }
    return render(request,'edit.html',context)
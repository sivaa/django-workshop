from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render

from todo.forms import TaskForm
from todo.models import Task


def get_tasks():
    tasks = Task.objects.all()
    return tasks

def tasks(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': get_tasks(), 'form': TaskForm()})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                task = Task(**form.cleaned_data)
                task.save()
                message = "Task '%s' added successfully!" % task.name
                form = TaskForm()
            except IntegrityError:
                message = "Task '%s' already exists!" % task.name
        else:
            message = "There are errors in the given input"
        return render(request, "tasks.html", {'message': message, 'tasks': get_tasks(), 'form': form})
    return HttpResponse("Invalid Request")


def tasks_edit(request, task_id):
    if request.method == 'GET':
        try:
            Task = Task.objects.get(pk=task_id)
            form = TaskForm(initial={'name': Task.name})
        except:
            message = "Invalid Task. Edit Failed!"
            return render(request, "tasks.html", {'tasks': get_tasks(), 'message': message, 'form': TaskForm()})
        return render(request, "tasks_edit.html", {'form':form })
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task = Task.objects.get(pk=task_id)
            Task.name = data['name']
            Task.save()
            message = "Task %s modified successfully!" % data['name']
            form = TaskForm()
        else:
            message = "There are errors in the given input"
        return render(request, "tasks.html", {'message': message, 'tasks': get_tasks(), 'form': form})
    return HttpResponse("Invalid Request")

def tasks_remove(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=task_id)
        except:
            message = "Invalid Task. Delete Failed!"
            return render(request, "tasks.html", {'tasks': get_tasks(), 'message': message, 'form': TaskForm()})
        return render(request, "tasks_delete_confirm.html", {'task':task })
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            message = "Task '%s' deleted successfully!" % task.name
        except:
            message = "Invalid Task. Delete Failed!"
        return render(request, "tasks.html", {'message': message, 'tasks': get_tasks(), 'form': TaskForm()})
    return HttpResponse("Invalid Request")

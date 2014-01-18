import datetime

from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from todo.forms import TaskForm
from todo.models import Task
from django.contrib.auth.decorators import login_required


def get_tasks():
    tasks = Task.objects.all()
    return tasks

@login_required
def tasks(request):
    if request.method == 'GET':
        message = ''
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']
        return render(request, "tasks.html", {'tasks': get_tasks(), 'message': message, 'form': TaskForm(),'page':'All'})
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
            task = Task.objects.get(pk=task_id)
            form = TaskForm(initial={'name': task.name, 'priority': task.priority, 'last_date': task.last_date, 'done': task.done})
        except:
            message = "Invalid Task. Edit Failed!"
            return render(request, "tasks.html", {'tasks': get_tasks(), 'message': message, 'form': TaskForm()})
        return render(request, "tasks_edit.html", {'form':form })
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.get(pk=task_id)
            task = Task(**form.cleaned_data)
            task.pk = task_id
            task.save()
            message = "Task %s modified successfully!" % data['name']
            request.session['message'] = message
            return redirect('/tasks/')
        else:
            message = "There are errors in the given input"
            return render(request, "tasks_edit.html", {'message': message, 'form': form})
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
            request.session['message'] = message
            return redirect('/tasks/')

        except:
            message = "Invalid Task. Delete Failed!"
        return render(request, "tasks.html", {'message': message, 'tasks': get_tasks(), 'form': TaskForm()})
    return HttpResponse("Invalid Request")


def tasks_priority_high(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(priority = 'H'), 'form': TaskForm(),'page':'H'})
    return HttpResponse("Invalid Request")

def tasks_priority_low(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(priority = 'L'), 'form': TaskForm(),'page':'L'})
    return HttpResponse("Invalid Request")

def tasks_completed(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(done = True), 'form': TaskForm(),'page':'C'})
    return HttpResponse("Invalid Request")

def tasks_not_completed(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(done = False), 'form': TaskForm(),'page':'NC'})
    return HttpResponse("Invalid Request")

def tasks_overdue(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(done = False, last_date__lt = datetime.date.today()), 'form': TaskForm(),'page':'OD'})
    return HttpResponse("Invalid Request")

def tasks_due_today(request):
    if request.method == 'GET':
        return render(request, "tasks.html", {'tasks': Task.objects.filter(done = False, last_date = datetime.date.today()), 'form': TaskForm(),'page':'T'})
    return HttpResponse("Invalid Request")
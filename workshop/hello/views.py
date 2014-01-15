from django.shortcuts import render
from datetime import datetime

def hello1(request):
    # Just a Hello World
    return render(request, 'hello1.html')

def hello2(request):
    # Hello World with Current Time
    return render(request, 'hello2.html', {'current_time': datetime.now()})

def hello3(request):
    # Hello World with Query String
    name = request.GET.get('name', "Django")
    return render(request, 'hello3.html', {'name': name})

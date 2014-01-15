from django.http.response import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Hello World!")

def hello1(request):
    return HttpResponse("<h1> Hello World!</h1>")

def hello2(request):
    return HttpResponse("Hello World! at %s" % datetime.now())

def hello3(request):
    name = request.GET.get('name', "Django")
    return HttpResponse("Hello World! %s" % name)

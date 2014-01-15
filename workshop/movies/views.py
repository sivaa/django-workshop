from django.shortcuts import render

from movies.models import Movie
from django.http.response import HttpResponse

def movies(request):
    if request.method == 'GET':
        return render(request, "movies.html")
    if request.method == 'POST':
        name = request.POST.get('name', None)
        Movie.objects.create(name=name)
        return HttpResponse("Movie '%s' added successfully!" % name)
    return HttpResponse("Invalid Request")
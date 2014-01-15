from django.shortcuts import render

from movies.models import Movie
from django.http.response import HttpResponse


def get_movies():
    movies = Movie.objects.all()
    return movies

def movies(request):
    if request.method == 'GET':
        return render(request, "movies.html", {'movies': get_movies()})
    if request.method == 'POST':
        name = request.POST.get('name', None)
        Movie.objects.create(name=name)
        message = "Movie '%s' added successfully!" % name
        return render(request, "movies.html", {'message': message, 'movies': get_movies()})
    return HttpResponse("Invalid Request")

def movies_remove(request):
    if request.method == 'GET':
        movie_id = request.GET.get('id', None)
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        message = "Movie '%s' deleted successfully!" % movie.name
        return render(request, "movies.html", {'message': message, 'movies': get_movies()})
    return HttpResponse("Invalid Request")

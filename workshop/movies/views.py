from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def get_movies():
    movies = Movie.objects.all()
    return movies

def movies(request):
    if request.method == 'GET':
        return render(request, "movies.html", {'movies': get_movies()})
    if request.method == 'POST':
        name = request.POST.get('name', None)
        if len(name.strip()) == 0:
            message = "Please enter a movie  name"
        elif len(name.strip()) < 3:
            message = "Not enough words!"
        else:
            try:
                Movie.objects.create(name=name)
                message = "Movie '%s' added successfully!" % name
            except IntegrityError:
                message = "Movie '%s' already exists!" % name
        return render(request, "movies.html", {'message': message, 'movies': get_movies()})
    return HttpResponse("Invalid Request")

def movies_remove(request):
    if request.method == 'GET':
        movie_id = request.GET.get('id', None)
        try:
            movie = Movie.objects.get(pk=movie_id)
            movie.delete()
            message = "Movie '%s' deleted successfully!" % movie.name
        except:
            message = "Invalid Movie. Delete Failed!"
        return render(request, "movies.html", {'message': message, 'movies': get_movies()})
    return HttpResponse("Invalid Request")

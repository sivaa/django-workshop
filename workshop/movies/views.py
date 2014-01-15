from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render

from movies.models import Movie
from movies.forms import MovieForm


def get_movies():
    movies = Movie.objects.all()
    return movies

def movies(request):
    if request.method == 'GET':
        return render(request, "movies.html", {'movies': get_movies(), 'form': MovieForm()})
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            try:
                Movie.objects.create(name=name)
                message = "Movie '%s' added successfully!" % name
            except IntegrityError:
                message = "Movie '%s' already exists!" % name
        else:
            message = "There are errors in the given input"
        return render(request, "movies.html", {'message': message, 'movies': get_movies(), 'form': form})
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
        return render(request, "movies.html", {'message': message, 'movies': get_movies(), 'form': MovieForm()})
    return HttpResponse("Invalid Request")

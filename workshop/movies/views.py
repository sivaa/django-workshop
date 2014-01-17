from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from movies.forms import MovieForm
from movies.models import Movie


def get_movies():
    movies = Movie.objects.all()
    return movies

def movies(request):
    if request.method == 'GET':
        message = ''
        if 'message' in request.session:
            message = request.session['message']
            del request.session['message']
        return render(request, "movies.html", {'movies': get_movies(), 'message': message, 'form': MovieForm()})
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            try:
                Movie.objects.create(name=name)
                message = "Movie '%s' added successfully!" % name
                form = MovieForm()
            except IntegrityError:
                message = "Movie '%s' already exists!" % name
        else:
            message = "There are errors in the given input"
        return render(request, "movies.html", {'message': message, 'movies': get_movies(), 'form': form})
    return HttpResponse("Invalid Request")


def movies_edit(request, movie_id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=movie_id)
            form = MovieForm(initial={'name': movie.name})
        except:
            message = "Invalid Movie. Edit Failed!"
            return render(request, "movies.html", {'movies': get_movies(), 'message': message, 'form': MovieForm()})
        return render(request, "movies_edit.html", {'form':form })
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            movie = Movie.objects.get(pk=movie_id)
            movie.name = data['name']
            movie.save()
            message = "Movie %s modified successfully!" % data['name']
            request.session['message'] = message
            return redirect('/movies/')

        else:
            message = "There are errors in the given input"
            return render(request, "movies_edit.html", {'message': message, 'form': form})
        return render(request, "movies.html", {'message': message, 'movies': get_movies(), 'form': form})
    return HttpResponse("Invalid Request")

def movies_remove(request, movie_id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=movie_id)
        except:
            message = "Invalid Movie. Delete Failed!"
            return render(request, "movies.html", {'movies': get_movies(), 'message': message, 'form': MovieForm()})
        return render(request, "movies_delete_confirm.html", {'movie':movie })
    if request.method == 'POST':
        try:
            movie = Movie.objects.get(pk=movie_id)
            movie.delete()
            message = "Movie '%s' deleted successfully!" % movie.name
            request.session['message'] = message
            return redirect('/movies/')
        except:
            message = "Invalid Movie. Delete Failed!"
        return render(request, "movies.html", {'message': message, 'movies': get_movies(), 'form': MovieForm()})
    return HttpResponse("Invalid Request")

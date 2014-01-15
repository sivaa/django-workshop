from django.contrib import admin

from movies.models import Movie
from movies.forms import MovieForm

class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

admin.site.register(Movie, MovieAdmin)